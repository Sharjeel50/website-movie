import json
import requests

def SeriesData():
    SeriesURL = "https://tv-v2.api-fetch.website/shows/1"
    SeriessResponse = requests.get(SeriesURL, headers= {'Content-Type': 'application/json; charset=utf-8'})
    SeriesDumpedData = json.dumps(SeriessResponse.json())
    SeriesLoadedData = json.loads(SeriesDumpedData)

    return Series


def MovieData():

    with open('includes/MovieData.json','r') as f:
        Data = json.loads(f.read())

    Movies = []

    for i in range(100):
        MovieDataDict = {
                            'Title': Data[i]['Title'],
                            'ID': Data[i]['ID'],
                            'IMDb_ID': Data[i]['IMDb_ID'],
                            'Year': Data[i]['Year'],
                            'MovieInfo': Data[i]['MovieInfo'],
                            'Genres': Data[i]['Genres'],
                            'Certification': Data[i]['Certification'],
                            'Percentage': Data[i]['Percentage'],
                            'Votes': Data[i]['Votes'],
                            'Watching': Data[i]['Watching'],
                            'TenEighty': Data[i]['1080p'],
                            'Filesize-1080p': Data[i]['Filesize-1080p'],
                            'Peer-1080p': Data[i]['Peer-1080p'],
                            'Seed-1080p': Data[i]['Seed-1080p'],
                            'SevenTwenty': Data[i]['720p'],
                            'Filesize-720p': Data[i]['Filesize-720p'],
                            'Peer-720p': Data[i]['Peer-720p'],
                            'Seed-720p': Data[i]['Seed-720p'],
                            'Image': Data[i]['Image']
                        }

        Movies.append(MovieDataDict)

    return Movies



#MoviesURL = "https://tv-v2.api-fetch.website/movies/1"
#MoviesResponse = requests.get(MoviesURL, headers= {'Content-Type': 'application/json; charset=utf-8'})
#MoviesDumpedData = json.dumps(MoviesResponse.json())
#MoviesLoadedData = json.loads(MoviesDumpedData)
