def Bubble_Sort(arg):
    n=len(arg)
    for i in range(n):
        for j in range(n-1,i,-1):
          if arg[j] < arg[j-1]:
              tmp = int(arg[j])
              arg[j]=int(arg[j-1])
              arg[j-1]=tmp
    return arg

Bubble_Sort([3,1,5,100,90,1000])
