

class Person():
    
    
    
    def __init__ (self, first_name, last_name, age, address):
        self.first_name= first_name
        self.last_name= last_name
        self.age= age;
        self.address= address
    
    def printString(self):
        return '{}{}{}{}'.format(self.first_name,self.last_name, self.age, self.address)
    
    def toUpper(self):
        self.printString
        print (self. printString().upper())

person1= Person()
person1.first_name=input(str("enter the first name of the person  "))
person1.last_name= input(str("enter the last name of the person  "))
person1.age= input(str("enter the age of the person  "))
person1.address= input(str("enter the address of the perso  "))

print(person1.first_name)
print(person1.last_name)
print(person1.age)
print(person1.address)

person1.toUpper()