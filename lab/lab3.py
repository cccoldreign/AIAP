import json

with open('/Users/coldreign/code/Study/AIAP/lab/countries.json', 'r') as countries:
    data = json.load(countries)

print(list(map(lambda x: x.lower(), data)))

print(list(filter(lambda x: "land" not in x, data)))