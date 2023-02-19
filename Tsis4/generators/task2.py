
 #  even numbers between 0 and n

def even_numbers(n):
   
    for i in range(0, n):
        if  i%2==0:
            yield i
        
# get input from user
n = int(input("Enter a number: "))

print(*even_numbers(n), sep=", ")
