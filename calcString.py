def calcString(str):
    strList = str.split("+")
    result=0
    for i in range(len(strList)):
        result += int(strList[i])
    return(result)

    print(calcString("1+3+7"))
