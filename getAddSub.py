def getAddSub(s):
    b_num = ''
    b_remain= ''
    for i in range(0, len(s)):
        if s[i] == '+': break
        elif s[i] == '-': break
        else:
          b_num += s[i]
          i=i+1
        b_remain = s[i:]
    return b_num,b_remain
