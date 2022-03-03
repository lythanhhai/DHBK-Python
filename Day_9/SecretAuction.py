from Art import logo

print(logo)

end_game = False
listUser = []

while not end_game:
    yourName = input("What is your name? ")
    yourBid = float(input("What is your bid? "))

    dict = {}
    dict["name"] = yourName
    dict["bid"] = yourBid

    listUser.append(dict)

    choice = input("Are there any other bidders? type 'yes' or 'no' ")

    if choice == 'yes':
        continue
    else:
        max = listUser[0]["bid"]
        res = {}
        for user in listUser:
            if max < user["bid"]:
                res["name"] = user["name"]
                res["bid"] = user["bid"]
                max = user["bid"]
        print(max, res, sep=" and ")
        break