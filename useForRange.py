list = [2,1,8,9,4,45,78,52,12]

def listCounter(listToCount):
    sum = 0
    for i in range(len(listToCount)):
        sum += listToCount[i]
        print(listToCount[i], sum)

listCounter(list)
