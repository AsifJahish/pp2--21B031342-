

class Shape():
    
    def __init__ (self):
        pass
    
    def __str__(self):
        print( self.__class__.__name__)
        
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length=length
        
    
    def area(self):
        return self.length*self.length

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length=length
        self.width=width
    def area(self):
        return self.length* self.width

r=int(input("for sqaure enter 1 and for ractangle enter 2   "))
if r==1:
    b=int(input("enter the length of the square   "))
    a=Square(b)
    a.__str__()
    print (a.area())
elif r==2:
    b=int(input("enter the length of the ractangle   "))
    c=int(input("enter the width of of the rechtangle   "))
    d=Rectangle(b,c)
    b.__str__()
    print (d.area())
