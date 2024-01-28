# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 15:13:40 2024

@author: Yu Chenxi
"""

class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"
    
    def evaluate(self, value):
        return value

class Int:
    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return str(self.i)
    
    def evaluate(self, value):
        return self.i

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)
    
    def evaluate(self, value):
        return self.p1.evaluate(value) + self.p2.evaluate(value)
    
class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " - " + repr(self.p2)
    
    def evaluate(self, value):
        return self.p1.evaluate(value) - self.p2.evaluate(value)

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p1, Add):
            if isinstance(self.p2, Add):
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, Add):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        if isinstance(self.p1, Sub):
            if isinstance(self.p2, Sub):
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, Sub):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        return repr(self.p1) + " * " + repr(self.p2)
    
    def evaluate(self, value):
        return self.p1.evaluate(value) * self.p2.evaluate(value)
    

class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p1, Add):
            if isinstance(self.p2, Add):
                 return "( " + repr(self.p1) + " ) / ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) / " + repr(self.p2)
        if isinstance(self.p2, Add):
            return repr(self.p1) + " / ( " + repr(self.p2) + " )"
        #return repr(self.p1) + " / " + repr(self.p2)
        if isinstance(self.p1, Sub):
            if isinstance(self.p2, Sub):
                 return "( " + repr(self.p1) + " ) / ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) / " + repr(self.p2)
        if isinstance(self.p2, Sub):
            return repr(self.p1) + " / ( " + repr(self.p2) + " )"
        return repr(self.p1) + " / " + repr(self.p2)
    
    def evaluate(self, value):
        return self.p1.evaluate(value) / self.p2.evaluate(value) if self.p2.evaluate(value) != 0 else 'Division by zero!'
    
    
poly = Add(Add(Int(4), Int(3)), Add(X(), Mul(Int(1), Add(Mul(X(), X()), Int(1)))))
print(poly)
print(poly.evaluate(-1))

poly2 = Sub( Sub( Int(4), Int(3)), Sub( X(), Div( Int(1), Sub( Div(X(), X()), Int(1)))))
#print(poly2)

poly3 = Add( Add( Int(4), Int(3)), Add( X(), Div( Int(1), Add( Div(X(), X()), Int(1)))))
#print(poly3)

poly4 = Sub( Sub( Int(4), Int(3)), Sub( X(), Mul( Int(1), Sub( Mul(X(), X()), Int(1)))))
#print(poly4)