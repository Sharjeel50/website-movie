import json

with open('MovieData.json','r') as f:
    Data = json.load(f)

for i in range(12):
    print(Data)
