def getNum1(BL):
    b_num = []
    b_remain = []
    n=0
    a=s
    for i in range(0,len(BL)):
        if BL[i] == n:
            while n <= 9:
                print('True')
                b_num += str(BL[i])
                i += 1
        else:
            print('False')
            break
            
    for a in range(s,len(BL)):
        b_remain += str(BL[a])

    return b_num
    return b_remain
