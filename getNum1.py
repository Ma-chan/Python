def getNum(s):
    b_num = []
    b_remain = []
    for i in range(0,len(s)):
        if s[i] == '0':
            b_num += s[i]
            i = i + 1
        elif s[i] == '1':
            b_num += s[i]
            i = i + 1
        elif s[i] == '2':
            b_num += s[i]
            i = i + 1
        elif s[i] == '3':
            b_num += s[i]
            i = i + 1
        elif s[i] == '4':
            b_num += s[i]
            i = i + 1
        elif s[i] == '5':
            b_num += s[i]
            i = i + 1
        elif s[i] == '6':
            b_num += s[i]
            i = i + 1
        elif s[i] == '7':
            b_num += s[i]
            i = i + 1
        elif s[i] == '8':
            b_num += s[i]
            i = i + 1
        elif s[i] == '9':
            b_num += s[i]
            i = i + 1
        elif s[i] == '+':
            b_remain += s[i]
            i = i + 1
            break
        elif s[i] == '-':
            b_remain += s[i]
            i = i + 1
            break
    for i in range(i,len(s)):
        if s[i] == '0':
            b_remain += s[i]
            i = i + 1
        elif s[i] == '1':
            b_remain += s[i]
            i = i + 1
        elif s[i] == '2':
            b_remain += s[i]
            i = i + 1
        elif s[i] == '3':
            b_remain += s[i]
            i = i + 1
        elif s[i] == '4':
            b_remain += s[i]
            i = i + 1
        elif s[i] == '5':
            b_remain += s[i]
            i = i + 1
        elif s[i] == '6':
            b_remain += s[i]
            i = i + 1
        elif s[i] == '7':
            b_remain += s[i]
            i = i + 1
        elif s[i] == '8':
            b_remain += s[i]
            i = i + 1
        elif s[i] == '9':
            b_remain += s[i]
            i = i + 1
        elif s[i] == '+':
            b_remain += s[i]
            i = i + 1
        elif s[i] == '-':
            b_remain += s[i]
            i = i + 1
        else:
            break
    return b_num,b_remain

