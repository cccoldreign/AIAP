import numpy as np

firstList = np.random.randint(-10, 10, 7).tolist()
secondList = np.random.randint(-10, 10, 7).tolist()
thirdList = []

print("", firstList,'\n', secondList)

for i in range(len(firstList)):
    if i % 2 == 0:
        thirdList.append(firstList[i])
    else:
        thirdList.append(secondList[i])
# for i in range(len(secondList)):
#     if i % 2 != 0:
#         thirdList.append(secondList[i])

print("", thirdList)