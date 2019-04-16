import json

with open('MovieData.json','r') as f:
    Data = json.load(f)

for i in range(3):
    print(Data[i]['1080p'])
