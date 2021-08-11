list1 = [2,1,8,9,4,45,78,52,12]

def listCounter(listToCount):
    listC = 0
    for i in range(len(listToCount)):
        listC += listToCount[i]
        print(listToCount[i], listC)

listCounter(list1)
