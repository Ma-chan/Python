def getNum(m):
   b_num = []
   n=0
   for i in range(0,len(m)):
     for n in range(10):
      if int(m[i]) == n:
        print('True')
        b_num.append(n)
        print(b_num)
      else:
        break
        print('False')
        print(b_num)
   return b_num
