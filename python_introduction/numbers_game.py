# This game is about guessing numbers correctly
import random

secret_number = random.randint(1,10)
# print("I'm thinking of a number between 1 and 10. Can you guess it?")
guess = int(input("I'm thinking of a number between 1 and 10. Can you guess it?"))
guess_counter = 0

while guess != secret_number:
    match guess:
        case int():
            if guess > secret_number:
                print("Oops, your guess is a bit high. Try again!")
                guess_counter += 1
                guess = int(input("Make another guess"))
            elif guess < secret_number:
                print("Nope, your guess is a bit low. Give it another shot!")
                guess_counter += 1
                guess = int(input("Make another guess"))
        case _:
            print("Enter a figure between 1 and 10")  
else:
    print("Congratulations, you guessed it!")
    guess_counter += 1
print("you guessed ", guess_counter, "time(s)")

