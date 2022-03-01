import random

word_list = ["ardvark", "baboon", "camel"]

# chọn ngẫu nhiên 1 từ
word_choice = random.choice(word_list)
letter_enter = input("Please enter 1 letter to check answer: ")

for i in word_choice:
    if i == letter_enter:
        print("Right")
    else:
        print("Wrong")

