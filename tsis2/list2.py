


my_list= ["first_name", "last_name","address","education_degree", "University"]


for i in range (len(my_list)):
    print(my_list[i], end=" ")

print("\n")


    
for i in my_list:
    print(i, end=" ")

print("\n")

i=0
while i<len(my_list):
    print(my_list[i], end="  ")
    i+=1;
print("\n")

[print(x, end="  ") for x in my_list]

print("\n")

your_list=[]

for i in my_list:
    if "a" in i:
        your_list.append(i)
print(your_list)


new_list= [i for i in my_list if "s" in i]

print(new_list)


