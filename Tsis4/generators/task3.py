

 # generate numbers divisable on 3 and 4 between 0 and n

def divisable_3_4(n):

    for i in range(0 ,n):
        if i%3==0 and i%4==0:
            yield i


number= int(input("enter a number that you want to    "))

ab =divisable_3_4(number)

for a in(ab):
 print(a)