dict1 = {
    '[1]': 1,
    '[2]': 2,
    '[3]': 3,
    '[4]': 4.2
}
dict2 = {
    '[6]': 6,
    '[2]': 2,
    '[5]': 5,
    '[4]': 4.2
}

print(set(dict1.items()).intersection(set(dict2.items())))