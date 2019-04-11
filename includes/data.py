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
        Data = json.loads(f)

    Movies = []

    for i in range:
        MovieDataDict = {
                            'Title': Data[i]['Title'],
                            'ID': Data[i]['_id'],
                            'IMDb_ID': Data[i]['imdb_id'],
                            'Year': Data[i]['year'],
                            'MovieInfo': Data[i]['synopsis'],
                            'Genres': Data[i]['genres'][:],
                            'Certification': Data[i]['certification'],
                            'Percentage': Data[i]['rating']['percentage'],
                            'Votes': Data[i]['rating']['votes'],
                            'Watching': Data[i]['rating']['watching'],
                            '1080p': Data[i]['torrents']['en']['1080p']['url'],
                            'Filesize-1080p': Data[i]['torrents']['en']['1080p']['filesize'],
                            'Peer-1080p': Data[i]['torrents']['en']['1080p']['peer'],
                            'Seed-1080p': Data[i]['torrents']['en']['1080p']['seed'],
                            '720p': Data[i]['torrents']['en']['720p']['url'],
                            'Filesize-720p': Data[i]['torrents']['en']['720p']['filesize'],
                            'Peer-720p': Data[i]['torrents']['en']['720p']['peer'],
                            'Seed-720p': Data[i]['torrents']['en']['720p']['seed'],
                            'Image': Data[i]['images']['poster']
                        }

        Movies.append(MovieDataDict)

    return Movies



#MoviesURL = "https://tv-v2.api-fetch.website/movies/1"
#MoviesResponse = requests.get(MoviesURL, headers= {'Content-Type': 'application/json; charset=utf-8'})
#MoviesDumpedData = json.dumps(MoviesResponse.json())
#MoviesLoadedData = json.loads(MoviesDumpedData)
