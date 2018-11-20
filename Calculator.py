import re

def isnum():

  if int(piyo) == True:
    return 1
  else:
    return 0

def calculator(str):

    strarr = re.split("[+,-,*]",strarr)

    if strarr[i] == "+":
        return int(result)
    elif strarr[i] == "-":
        return int(result)
    elif strarr[i] == "*":
        return int(result)

    por = []
    por = list(input().split())
    stk=[]

    for i in por:
        if isnum(i) == int:
