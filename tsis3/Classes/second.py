

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

b=int(input("enter the length of the square   "))

a=Square(b)
a.__str__()
print (a.area())
        