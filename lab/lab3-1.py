import json
from functools import reduce

with open('/Users/coldreign/code/Study/AIAP/lab/countries.json', 'r') as countries:
    data = json.load(countries)

def categorize_countries(sample):
    def print_countries(countries):
        return list(filter(lambda x: sample in x, countries))
    return print_countries

print(list(map(lambda x: x.lower(), data)))

print(list(filter(lambda x: "land" in x, data)))

print(list(filter(lambda x: len(x) == 6, data)))

print(list(filter(lambda x: x.startswith('E'), data)))

NorthCountry = ['Финляндия', 'Швеция', 'Дания', 'Норвегия', 'Исландия']
print(reduce(lambda x,y: x + ", "+ y, NorthCountry) + " являются странами Северной Европы.")

print(list(filter(lambda x: "land" in x, list(map(lambda x: x.lower(), data)))))

print(categorize_countries("ia")(data))

with open("countries-data.json", "r", encoding="utf-8") as file:
    countries_data = json.load(file)

sortedName = sorted(countries_data, key=lambda x: x['name'])
sortedCapital = sorted(countries_data, key=lambda x: x['capital'])
sortedPopulation = sorted(countries_data, key=lambda x: x['population'])

all_languages = [language for country in countries_data for language in country['languages']]
language_count = [(language, all_languages.count(language)) for language in set(all_languages)]
topLanguages = sorted(language_count, key=lambda x: x[1], reverse=True)[:10]

sorted_population_desc = sorted(countries_data, key=lambda x: x['population'], reverse=True)
top_populated_countries = sorted_population_desc[:10]

