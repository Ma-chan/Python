def getOperator(s):
    a_op = ''
    a_num = ''
    if s[0] == '+':
        a_op = s[0]
        a_num = s[1:]
    elif s[0] == '-':
        a_op = s[0]
        a_num = s[1:]
    else:
        a_op = ''
        a_num = s[0:]
    return a_op,a_num
