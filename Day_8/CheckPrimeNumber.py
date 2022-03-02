import math
#Write your code below this line 👇
def prime_checker(number):
  if number <= 0:
    return False
  elif number <= 2:
    return True
  else:
    for i in range(2, int(math.sqrt(n)) + 1):
      if n % i == 0:
        return False
    return True
  
#Write your code above this line 👆
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
if prime_checker(number=n) == True:
    print("It is a prime number!")
else:
    print("It is not a prime number!")

