import numpy as np

list = [12.3, "1", 1, "12.3", 13, 13, 13]

for i in range(len(list)):
    list[i] = str(list[i])

list = sorted(set(list))

print(list)