import re
def strMath(str):
    global strarr
    input1="1足す3"
    strarr = re.split('[足す,引く]',input1)
    for i in range(len(strarr)):
        if strarr[i] != "足す":
            'sum += int(strarr[i])'
        if strarr[i] != "引く":
            'sum -= int(strarr[i])'
    return sum
