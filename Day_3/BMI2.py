height, weight = map(float, input().split())

BMI = round(weight / (height ** 2), 2)

if BMI < 18.5:
    print(f'Your bmi is {BMI}, You are underweight')
elif BMI < 25:
    print(f'Your bmi is {BMI}, You are a normal weight')
elif BMI < 30:
    print(f'Your bmi is {BMI}, You are overweight')
elif BMI < 35:
    print(f'Your bmi is {BMI}, You are obese')
else:
    print(f'Your bmi is {BMI}, You are obinically obese')