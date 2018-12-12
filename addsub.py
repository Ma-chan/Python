def addsub(s):
    sum=''
    for i in range(0,len(s)):
        if s[i] == '+':
            sum += s[i+1]
            i=i+1
        elif s[i] == '-':
            sum -= s[i+1]
            i=i+1
        else:
            sum = s[0:]
            break
    return sum
