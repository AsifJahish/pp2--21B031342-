


my_list= ['Ali', 'batur', 'jhan','wick']

for i in my_list:
    print(i, end=" ")
print("\n")


print(my_list) # access entire element


print(my_list[3])  # access only one element


# change element in list

my_list [0:3]= ["tom", "mohammad","ali"] # change a rane of element of the list

print(my_list)

my_list [1]= ["lenoard"]

print(my_list)


# how to add element in the list and where we can add to the list
# we can use insert and extend and append to add element in list\
    
    
my_list.append("jolie")

print(my_list)

my_list.insert (0,"basir")

print(my_list)


your_list =["baz", "nur", "Alfe"]

my_list.extend(your_list)

print(my_list)


# how to remove element from 
# to remove element we use three method pop remove and del


my_list.remove("baz");
print(my_list)


my_list.pop(1)
print(my_list)

my_list.pop()
print(my_list)



del my_list[1]
print(my_list)


your_list.clear()
print(your_list)


del my_list
print(my_list)

