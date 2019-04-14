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

    return Data
