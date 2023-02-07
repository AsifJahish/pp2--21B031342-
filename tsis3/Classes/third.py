



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f'({self.x}, {self.y})')

    def move(self,x,y):
        self.x += x
        self.y += y
        return x, y

    def dist(self, other):
        return (((self.x - other.x)**2 + (self.y - other.y)**2)**0.5)


x=int(input("enter the cordinate for x  "))
y = int(input("enter the coordinate for y   "))
a= Point(x,y)

a.show();
print(a.move(x,y))
print(a.dist)