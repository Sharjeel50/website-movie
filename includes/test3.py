import json

with open('MovieData.json','r') as f:
    Data = json.load(f)

Counter = 0
for i in range(50):
    #print(Data[i]['Title'])
    print(Counter , Data[i]['Image'])

    Counter += 1
    <p>{{Movie.Filesize-1080p}}</p>
  <p>{{Movie.Peer-1080p}}</p>
  <p>{{Movie.Seed-1080p}}</p>
