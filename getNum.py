def getNum(m):
   w = []
   n = 0
   for i in range(0,len(m)):
     if int(m[i]) == n:
      while n <= 9:
        print('True')
        w += str(m[i])
        i += 1
     else:
        print('False')
        break
   return w
