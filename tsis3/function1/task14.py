

import random
from task13 import play_game

tries = 5
number = random.randint(1, 20)
while tries>3:
    guess = int(input("Take a guess "))   
    

play_game()