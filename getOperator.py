def getOperator(s):
    a_op=[]
    a_remain=[]

    for i in range(0,len(s)):
        if s[i] == '+':
          a_op = s[i]

        elif s[i] == '-':
          a_op = s[i]
        else:
          a_remain = s[i:]
          i=i+1
          break
    return a_op,a_remain
