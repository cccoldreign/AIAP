import json

data = '/Users/coldreign/code/Study/AIAP/practice/practice2/data.json'

with open(data, 'r') as file:
    date = json.load(file)

while True:
  search = input()

  for key,value in date.items():
    if value == search:
      print('key:',key)
      break
    else:
      print('ничего не найдено')
      break