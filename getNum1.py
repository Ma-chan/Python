def getNum(a):
    b_num = []
    n=0
    for i in range(0, len(a)):
        while n <= 9:
            if a[i] == n:
              print('True')
              print(a[i],n)
              b_num += a[i]
            elif str(a[i]) == '+':
                print('False')
                break
            elif str(a[i]) == '-':
                print('False')
                break
    return b_num

    b_remain = []
    for b in range(k,len(a)):
        b_remain += [a[b]]
        print(b_remain)
    return b_remain
