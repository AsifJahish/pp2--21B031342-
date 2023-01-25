x=10;
print(x)

a= "your name"
print(a)


b= int(3)
print(b)

c= float(2.4)
print(c)

d= str("my_name")
print(d)

e= complex(121221j)
print(e)


def finex():
    print(x)

finex()



def globalx():
    global r
    r=100   
    
    
globalx()

print (r)

# instead of global we can use make like this as well



y =10

def findY():
    globalY= y
    print(y)
    
findY()