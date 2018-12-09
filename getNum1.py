def getNum(a):
    b_num = []
    n=0
    for i in range(0, len(a)):
        print(a[i], n)
        if a[i] == n:
            while n<= 9:
                print('True')
                b_num += [a[i]]
        else:
            print('False')
            break
        return b_num

    b_remain = []
    for b in range(k,len(a)):
        b_remain += [a[b]]
    return b_remain
