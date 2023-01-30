
i=0; 
a= "hello world"

# print all letter except  e and o


while i< len(a):
    if a[i]== "e" or a[i]== "o":
        
        i+=1;
        continue
    print(a[i], end= " " )
    i+=1;
    
print("\n")