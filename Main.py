import os
import json
import hashlib
import requests
from flask import Flask, render_template, url_for, request, redirect
from includes.data import MovieData, SeriesData
from wtforms import StringField, PasswordField, BooleanField, validators
from flask_wtf import Form
from wtforms.validators import InputRequired, Email, Length
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo

app = Flask(__name__)
app.static_folder = 'static'

app.config["MONGO_URI"] = "mongodb://localhost:27017/Users"
mongodb = PyMongo(app)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

bootstrap = Bootstrap(app)

# Home
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@app.route('/')
def Home():
    Data = MovieData()
    testMovies = []
    for i in range(50):
        testMovies.append(Data[i])

    return render_template('Home.html', LoopMovies = testMovies) # Running function to get movie data nad need to make sure i loop through series to display them too


# Movies Page
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@app.route('/Movies') # TODO
def Movies():
    return render_template('Movies.html', LoopMovies = MovieData()) # Running function to get movie data


# Series Page
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@app.route('/Serie/<string:id>') # TODO
def Serie():

        # Data = MovieData()
        # for i in range(50):
        #     if Data[i]['ID'] == str(id):
        #         Movie = Data[i]
        #

    return render_template('Series.html') # Running function to get movie data


# Individual Serie Page
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@app.route('/Series') #TODO
def Series():
    return render_template('Series.html') # Running function to get movie data


# Individual Movie Page
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@app.route('/Movie/<string:id>/') # To fix once the user clicks on next button to
def Movie(id):
    Data = MovieData()
    for i in range(50):
        if Data[i]['ID'] == str(id):
            Movie = Data[i]

    return render_template('Movie.html', Movie = Movie) # Running function to get movie data

# Genre Page
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@app.route('/Genre/<string:genre>')
def GenrePage(genre):
    Data = MovieData()
    GenreMovies = []
    for i in range(len(Data)):
        if str(genre) in Data[i]['Genres']:
            GenreMovies.append(Data[i])

    return render_template('Genre.html', ChoseGenre = GenreMovies)

# Login
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class LoginForm(Form):
    username = StringField('username', validators = [InputRequired(), Length(min = 4, max = 15)])
    password = PasswordField('password', validators = [InputRequired(), Length(min = 6, max = 15)])
    remember = BooleanField('remember me')

@app.route("/Login")
def Login():
    form = LoginForm(request.form)
    return render_template('Login.html', form = form)  # Need to make sure user gets logged in on username and password verification then redirect


# Register
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class RegisterFrom(Form):
    username = StringField('Username', validators = [InputRequired(), Length(min = 4, max = 15)])
    email = StringField('Email', validators = [InputRequired(), Email(message = 'Invalid Email'), Length(max = 30)])
    password = StringField('Password', validators = [InputRequired(), PasswordField('Password', [validators.DataRequired(), validators.EqualTo('Confirm', message = "Passwords do not match")]),Length(min = 6, max = 15)])
    confirm = PasswordField('Confirm Password')

@app.route("/Register", methods = ['GET', 'POST'])
def Register():
    usersDatabase = mongodb.db.Users
    form = RegisterFrom(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = hashlib.sha256(form.password.data.encode('utf-8')).hexdigest()
        usersDatabase.insert({'Username': username, 'Email': email, 'Password': password})

        print("User Added to database")

        return redirect(url_for('Home'))

    return render_template('Register.html', form = form)

       # if mongo.db.users.find_one({'username': request.form['Username']}) is None:
           # pass

    #return render_template('Register.html', form = form)



# Contact us Page
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Contact_Us(Form):
    title = StringField('title', validators = [InputRequired(), Length(min = 5, max = 50)])
    content = StringField('content', validators = [InputRequired(), Length(max = 100)])

@app.route('/ContactUs', methods = ['GET', 'POST'])
def Contactus():
    form = RegisterFrom(request.form)
    # if request.method = 'POST' and form.validate():
    #     return render_template('ContactUs.html', form = form)
    return render_template('ContactUs.html', form = form)



# Dont mess with this shit
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


if __name__ == '__main__':
    app.run(debug=True)
