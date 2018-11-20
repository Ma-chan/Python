import re
def strMath(str):
   global BL
   BL = re.split('[tasu,hiku]', str)
   tasu = BL[0]
   hiku = BL[0]
   sum = 0

   for i in range(len(BL)):
     if 'tasu' != BL[i]:
      "sum += int(BL[i])"
     elif 'hiku' != BL[i]:
      "sum -= int(BL[i])"
   return sum
