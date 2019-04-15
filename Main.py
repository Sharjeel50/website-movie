import os
import json
import requests
from flask import Flask, render_template, url_for
from includes.data import MovieData, SeriesData
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo

app = Flask(__name__)
app.static_folder = 'static'

app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

bootstrap = Bootstrap(app)

@app.route('/')
def Home():
    Data = MovieData()
    testMovies = []
    for i in range(50):
        testMovies.append(Data[i])

    return render_template('Home.html', LoopMovies = testMovies) # Running function to get movie data nad need to make sure i loop through series to display them too

@app.route('/Movies')
def Movies():
    return render_template('Movies.html', LoopMovies = MovieData()) # Running function to get movie data


@app.route('/Movie/<string:id>/')
def Movie(id):
    Data = MovieData()
    for i in range(50):
        if Data[i]['ID'] == str(id):
            Movie = Data[i]

    return render_template('Movie.html', Movie = Movie) # Running function to get movie data


@app.route('/Genre/<string:genre>')
def GenrePage(genre):
    Data = MovieData()
    GenreMovies = []
    for i in range(len(Data)):
        if str(genre) in Data[i]['Genres']:
            GenreMovies.append(Data[i])

    return render_template('Genre.html', ChoseGenre = GenreMovies)


class LoginForm(FlaskForm):
    username = StringField('username', validators = [InputRequired(), Length(min = 4, max = 15)])
    password = PasswordField('password', validators = [InputRequired(), Length(min = 6, max = 15)])
    remember = BooleanField('remember me')

class RegisterFrom(FlaskForm):
    username = StringField('Username', validators = [InputRequired(), Length(min = 4, max = 15)])
    email = StringField('Email', validators = [InputRequired(), Email(message = 'Invalid Email'), Length(max = 30)])
    password = StringField('Password', validators = [InputRequired(), Length(min = 6, max = 15)])


@app.route("/Login")
def Login():
    form = LoginForm()
    return render_template('Login.html', form = form)

@app.route("/Register", methods = ['GET', 'POST'])
def Register():
    form = RegisterFrom()
    if request.method == 'POST':
        if mongo.db.users.find_one({'username': request.form['Username']}) is None:
            pass



    return render_template('Register.html', form = form)

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
