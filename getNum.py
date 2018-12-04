def getNum(w):
    for i in range(0,len(w)):
     if w[i] == [0-9]:
         w.append(w[i])
     else:
         break
    return w[i]
