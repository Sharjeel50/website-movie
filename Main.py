import os
import json
import requests
from flask import Flask, render_template, url_for
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
    Data = MovieData()
    for i in range(50):
        if Data[i]['ID'] == str(id):
            Movie = Data[i]
    return render_template('Movie.html', Movie = Movie) # Running function to get movie data

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
