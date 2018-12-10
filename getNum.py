def getNum(a):
    b_num = []
    n=0
    for i in range(0, len(a)):
        for n in range(0,9):
            if int(a[i]) == n:
              print(a[i], n)
              print('True')
              b_num.extend(str(a[i]))
            elif str(a[i]) == '+':
                print('False')
                break
    return b_num
