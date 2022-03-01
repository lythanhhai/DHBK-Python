import random

word_list = ["ardvark", "baboon", "camel"]
lives = 6
# chọn ngẫu nhiên 1 từ
word_choice = random.choice(word_list)
print(f"You were chosen {word_choice}.")

endOfGame = False
while endOfGame == False:
    letter_enter = input("Please enter 1 letter to check answer: ")
    if letter_enter not in word_choice:
        lives -= 1
        print(lives)
        if lives == 0:
            print("You lose!")
            endOfGame = True


