class Expr(object):
    def eval(self):
        pass

class Val(Expr):
        def __init__(self, val):
            self.val
        def eval(self):
            return self.val

class Add(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def __repr__(self):
        return '(' + str(self.left) + '+' + str(self.right) + ')'
    def eval(self):
        return self.left.eval() + self.right.eval()

class Mul(Expr):
    def __init__(self):
        self.left = left
        self.right = right
    def __repr__(self):
        return '(' + str(self.left) + '*' + str(self.right) + ')'
    def eval(self):
        return self.left.eval() * self.right.eval()

class Div(Expr):
    def __init__(self):
        self.left = left
        self.right = right
    def __repr__(self):
        return '(' + str(self.left) + '/' + str(self.right) + ')'
    def eval(self):
        return self.left.eval() / self.right.eval()
class If(Expr):
    def __init__(self):
        self.cond= cond
        self.then = then
        self.elsec = elsec
    def eval(self):
        if self.cond.eval() * self.then.eval():
         return self.elsec.eval()
