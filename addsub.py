def addsub(s):
  left = ""
  right= ""
  sum = ""

  for i in range(0, len(s)):
      if s[i] == '+':
          left = s[0:i]
          right = s[i+1:]
          sum=int(left)+int(right)
          break
      elif s[i] == '-':
          left = s[0:i]
          right = s[i + 1:]
          sum = int(left)-int(right)
          break
      else:
          sum = left
          left = s[0:]
  return sum
