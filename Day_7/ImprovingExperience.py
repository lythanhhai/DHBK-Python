import random
import HangmanWord
import HangmanArt

word_choice = random.choice(HangmanWord.word_list)

print(HangmanArt.logo)

lives = 6
print(f"You were chosen {word_choice}.")

endOfGame = False
display = []
while endOfGame == False:
    letter_enter = input("Please enter 1 letter to check answer: ")

    if len(letter_enter) >= 2:
        print("Please enter a letter!")
        continue

    if letter_enter not in word_choice:
        lives -= 1
        print(f"There isn't any {letter_enter} and the life left: {lives}.")
        if lives == 0:
            print("You lose!")
            endOfGame = True
    else:

        if len(display) < len(word_choice): 
            for letter in word_choice:
                if letter_enter == letter:
                    display.append(letter)
                else:
                    display.append("_")
        else:
            for index in range(0, len(word_choice)):
                if display[index] == "_" and word_choice[index] == letter_enter:
                    display[index] = letter_enter

        if len(display) == len(word_choice):
            if "_" not in display:
                endOfGame = True
                print("You win!")
                break
        print(display)



