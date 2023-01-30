


fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


fruit = ("apple", "banana", "cherry", "strawberry", "raspberry")

(greens, yellows, *reds) = fruit

print(greens)
print(yellows)
print(reds)


thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
  
  
  tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)