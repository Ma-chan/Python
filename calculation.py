class Q:
   def __init__(self, a, b=1):
       self.a=a
       self.b=b
   def __repr__(self):
       if self.b==1:
        return str(self.a)
       return str(self.a)+'/'+str(self.b)

   def __add__(self, x):
       a=self.a
       b=self.b
       c=x.a
       d=x.b
       return Q(a*d+b*c,b*d)

   def __truediv__(self, x):
       if isinstance(x, int):
           return self / Q(x)
       a=self.a
       b=self.b
       c=x.a
       d=x.b
       return Q(a*d, b*c)

   def  __sub__(self,x):
       a=self.a
       b=self.b
       c = x.a
       d = x.b
       return Q(a*d-b*c,b*d)

   def __mul__(self,x):
       a = self.a
       b = self.b
       c = x.a
       d = x.b
       return Q(a * d * b * c, b * d)
   def __div__(self, x):
       a = self.a
       b = self.b
       c = x.a
       d = x.b
       return Q(a*d/b*c,b*d)
