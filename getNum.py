def getNum(s):
    b_num = []
    n=0
    for i in range(0, len(s)):
          if s[i] == n:
           while n <=9:
              print('True')
              print(s[i],n)
              b_num.extend(n)
          else:
              print('False')
              break
    return b_num
