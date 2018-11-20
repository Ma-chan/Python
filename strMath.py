import re
def strMath(BL):
   global BL
   BL = re.split('[tasu,hiku]', BL)
   tasu = BL[0]
   hiku = BL[0]
   sum = 0

   for i in range(0, len(BL)):
     if 'tasu' != BL[i]:
      "sum += int(BL[i])"
     elif 'hiku' != BL[i]:
      "sum -= int(BL[i])"
   print(sum)
