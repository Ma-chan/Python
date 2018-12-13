def muldiv(s):
    result = ""
    left = ""
    right = ""

    for i in range(0, len(s)):
        if s[i] == '*':
            left = s[0:i]
            right = s[i + 1:]
            result = int(left) * int(right)
            break
        elif s[i] == '/':
            left = s[0:i]
            right = s[i + 1:]
            result = int(left) / int(right)
            break
        else:
            result = left
            left = s[0:]
    return result
