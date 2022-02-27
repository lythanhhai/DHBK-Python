print("Welcome to treasure island", "Your mission is to find the treasure" , sep="\n")

firstChoise = input("What the direction do you want (left or right): ")

if firstChoise == "left":
    secondChoise = input("What the direction do you want continue(wait or swim): ")
    if secondChoise == "wait":
        thirdChoise = input("What the direction do you want continue(blue, red or yellow): ")
        if thirdChoise == "blue" or thirdChoise == "red":
            print("you WIn, congratulation!")
        else:
            print("game over")
    else:
        print("game over")
else:
    print("game over")