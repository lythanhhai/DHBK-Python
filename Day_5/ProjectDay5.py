import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
numbers = ['0', '1', '2', '3', '4']
symbols = ['!', '@', '#']

print("Welcome to the Pypassword generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_number = int(input(f"How many number would you like?\n"))
password = ""

for char in range(1, nr_letters + 1):
    password += random.choice(letters)
for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)
for char in range(1, nr_number + 1):
    password += random.choice(numbers)

random.shuffle(list(password))
print(password)