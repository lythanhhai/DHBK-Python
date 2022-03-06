#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

from numpy import number 

end_game = False
number_times = 0

def play(number):
        number_times = number
        print(f"You have {number_times} to try out")
        while number_times > 0:
            number_curent = int(input("Make a guess: "))
            number_times -= 1
            if number_curent > guessing_number:
                print("Too high")
                print(f"Left {number_times}")
                print("Guess again")
                continue
            elif number_curent < guessing_number:
                print("Too low")
                print(f"Left {number_times}")
                print("Guess again")
                continue
            else:
                print(f"You guessed correct. Congratulation! with {number - number_times} times try out")
                break

        return number_times

print("Welcome to the Number Guessing Game!")
guessing_number = random.randint(1, 100)
print(f"I'm thinking of a number between 1 and 100 is {guessing_number}")
while not end_game:
    your_choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if your_choice == "easy":
        if play(10) <= 0:
            print("You lose")
    elif your_choice == "hard":
        if play(5) <= 0:
            print("You lose")
    else:
        print("Please type correct!")
        continue

    if input("Enter 'q' to quit game: ") == "q":
        end_game = True