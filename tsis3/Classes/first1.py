
class StringOperation:
    
    def __init__(self):
        self.str= ""
    
    def getString(self):
        self.str= str(input("enter an string    "))
    
    def printString(self):
        print(self.str.upper())
    
    
a = StringOperation()
a.getString()
a.printString()
    
