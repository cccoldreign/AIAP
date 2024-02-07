tupleList = []
dict1 = {
    '[1]': 1,
    '[2]': 2,
    '(2)': 2,
    '[3]': 3,
    '[4]': 4.2,
    '[5]': 5,
    '/5/': 5
}
dict2 = {}

for key, value in dict1.items():
    if value in dict2:
        dict2[value].append(key)
    else:
        dict2[value] = [key]
for key, value in dict2.items():
    tupleList.append((key, value))

for i in dict1.items():
    print(i)
print('\n')
for i in tupleList:
    print(i)