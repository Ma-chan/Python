def getNum(a):
    b_num = []
    n=0
    b=0
    for i in range(0, len(a)):
        print(a[i], n)
        if a[i] == n:
            for b in range(0,9):
                print('True')
                b_num += [a[i]]
        else:
            print('False')
            break
        return b_num
