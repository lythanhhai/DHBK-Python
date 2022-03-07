import random
import Art
import Game_data

print(Art.logo)
comparerContinue = random.choice(Game_data.data)
end_game = False
count = 0
while not end_game:
    comparerCurrent = comparerContinue
    print(f"Compare A: {comparerCurrent['name']}, a {comparerCurrent['description']}, from {comparerCurrent['country']}")
    print(Art.vs)
    comparerContinue = random.choice(Game_data.data)
    print(f"Compare B: {comparerContinue['name']}, a {comparerContinue['description']}, from {comparerContinue['country']}")

    your_choice = input("Type Higher and Lower!: ")
    if your_choice == "Higher":
        if comparerCurrent['follower_count'] < comparerContinue['follower_count']:
            print("You guess correct add 1 times")
            count += 1
            print("continous")
        else:
            print("You lose!")
            end_game = True
    else:
        if comparerCurrent['follower_count'] > comparerContinue['follower_count']:
            print("You guess correct add 1 times")
            count += 1
            print("continous")
        else:
            print("You lose!")
            end_game = True

