

class Point(object):
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def shift(self, x, y):
        x+=x
        y+=y
        return self.x, self.y
    def __str__(self):
        return f"the codinate of x is {self.x} and the corinate of y is {self.y} and it move {self.shift()}"  

po= Point(1,2)
print(po.get_x())
print(po.get_y())
print(po.shift())
print(po.__str__())