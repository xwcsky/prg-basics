import json

with open("clothes.json", "r") as file:
    data = json.load(file)

for key,value in data.items():
    print(f"{key} : {value}")