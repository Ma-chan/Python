def getMaxMin(list):
    max=0
    min=100
    for i in range(len(list)):
        if max < list[i]:
            max = list[i]
        if min > list[i]:
            min = list[i]
    return max,min
    print(getMaxMin([3,1,4,1,5,9,2]))
