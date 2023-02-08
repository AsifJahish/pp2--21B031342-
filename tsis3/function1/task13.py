



import random

def play_game():
    number = random.randint(1, 20)
    tries = 5
    guess_count=0
    name= str(input("Hello! What is your name?  "))
    print(f"Well, {name} I am thinking of a number between 1 and 20. ")
   
    while tries > 0:

        guess = int(input("Take a guess   "))
        guess_count+=1
        if guess == number:
            print(f"Good job, {name} ! You guessed my number in { guess_count}  guesses!")
            break
            
        elif guess < number:
            print("The number is higher.")
        else:
            print("The number is lower.")
        tries -= 1
    if tries == 0:
        print("You ran out of tries. The number was", number)



play_game()
