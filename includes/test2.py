import requests
import json

for i in range(90,100):
    MoviesURL = f'https://tv-v2.api-fetch.website/movies/{i}'
    MoviesResponse = requests.get(MoviesURL, headers= {'Content-Type': 'application/json; charset=utf-8'})
    MoviesDumpedData = json.dumps(MoviesResponse.json())
    MoviesLoadedData = json.loads(MoviesDumpedData)

Movies = []

for i in range(len(MoviesLoadedData)):
    URL_1080p = ""
    Filesize_1080p = ""
    Peer_1080p = ""
    Seed_1080p = ""
    
    if '1080p' in MoviesLoadedData[i]['torrents']['en']:
        URL_1080p = MoviesLoadedData[i]['torrents']['en']['1080p']['url']
        Filesize_1080p = MoviesLoadedData[i]['torrents']['en']['1080p']['filesize']
        Peer_1080p = MoviesLoadedData[i]['torrents']['en']['1080p']['peer']
        Seed_1080p = MoviesLoadedData[i]['torrents']['en']['1080p']['seed']


    URL_720p = ""
    Filesize_720p = ""
    Peer_720p = ""
    Seed_720p = ""

    if '720p' in MoviesLoadedData[i]['torrents']['en']:
        URL_720p = MoviesLoadedData[i]['torrents']['en']['720p']['url']
        Filesize_720p = MoviesLoadedData[i]['torrents']['en']['720p']['filesize']
        Peer_720p = MoviesLoadedData[i]['torrents']['en']['720p']['peer']
        Seed_720p = MoviesLoadedData[i]['torrents']['en']['720p']['seed']
        
        
    MovieDataDict = {
                'Title': MoviesLoadedData[i]['title'],
                'ID': MoviesLoadedData[i]['_id'],
                'IMDb_ID': MoviesLoadedData[i]['imdb_id'],
                'Year': MoviesLoadedData[i]['year'],
                'MovieInfo': MoviesLoadedData[i]['synopsis'],
                'Genres': MoviesLoadedData[i]['genres'][:],
                'Certification': MoviesLoadedData[i]['certification'],
                'Percentage': MoviesLoadedData[i]['rating']['percentage'],
                'Votes': MoviesLoadedData[i]['rating']['votes'],
                'Watching': MoviesLoadedData[i]['rating']['watching'],
                '1080p': URL_1080p,
                'Filesize-1080p': Filesize_1080p,
                'Peer-1080p': Peer_1080p,
                'Seed-1080p': Seed_1080p,
                '720p': URL_720p,
                'Filesize-720p': Filesize_720p,
                'Peer-720p': Peer_720p,
                'Seed-720p': Seed_720p,
                'Image': MoviesLoadedData[i]['images']['poster']
            }
    
    Movies.append(MovieDataDict)
    
    print(f"{MovieDataDict['Title']}")



with open('MovieData.json','a') as f:
    json.dump(Movies,f,indent=2)
