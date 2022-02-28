import random 

def ReplaceBlank():
    count = 0
    word_list = ["ardvark", "baboon", "camel"]
    word_choose = random.choice(word_list)

    print(f"Pssst, the solution is {word_choose}.")

    display = []
    condition = 0
    while condition == 0:
        letter_enter = input("Please enter 1 letter to check answer(enter quit to exit): ").lower()

        if letter_enter == "quit":
            break


        if len(display) < len(word_choose): 
            for letter in word_choose:
                if letter_enter == letter:
                    display.append(letter)
                else:
                    display.append("_")
        else:
            for index in range(0, len(word_choose)):
                if display[index] == "_" and word_choose[index] == letter_enter:
                    display[index] = letter_enter

        if "_" not in display:
            break
        
        count = count + 1
        print(display)

    return count

ReplaceBlank()





