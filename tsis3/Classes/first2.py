

class Operation:
    
    def __init__(self, n):
        self.n = n
    
    def getString(self):
        self.n=str(input("Enter a string    "))
    
    def printString(self):
        return self.n
    

a=Operation()
a.getString()
print(f" the string is {a.printString()} and we need to change it to upper class in the second line \n {a.printString().upper()}")