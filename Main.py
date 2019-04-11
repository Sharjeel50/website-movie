import json
import requests
from flask import Flask, render_template
from includes.data import MovieData, SeriesData

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def Home():
    return render_template('Home.html', LoopMovies = MovieData()) # Running function to get movie data nad need to make sure i loop through series to display them too

@app.route('/Movies')
def Movies():
    return render_template('Movies.html', LoopMovies = MovieData()) # Running function to get movie data

@app.route('/Movie/<string:id>/')
def Movie(id):
    for i in MovieData():
        if str(i['ID']) == str(id):
            Movie = i
    return render_template('Movie.html', Movie = Movie) # Running function to get movie data


if __name__ == '__main__':
    app.run(debug=True)
