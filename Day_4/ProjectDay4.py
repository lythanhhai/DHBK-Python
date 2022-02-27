import random
user_choise = int(input("What do you choise? 0 for rock, 1 for paper and 2 for scissors: "))

computer_choise = random.randint(0, 2)

if user_choise >= 3 or user_choise < 0:
    print("User enter invalid number")
elif user_choise == 0 and computer_choise == 2:
    print("you win!")
elif user_choise == 2 and computer_choise == 0:
    print("you lose!")
elif user_choise < computer_choise:
    print("you lose!")
elif user_choise > computer_choise:
    print("you win!")
elif user_choise == computer_choise:
    print("It's a draw!")

