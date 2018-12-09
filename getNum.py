def getNum(a):
   b_num = []
   n=0
   for i in range(len(a)):
      if a[i] == n:
       for n in range(0, 9):
        print('True')
        b_num += [int(a[i])]
        return b_num
      else:
        print('False')
        return b_num
        break
