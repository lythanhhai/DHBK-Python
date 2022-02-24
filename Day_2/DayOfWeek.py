age = int(input("How old are you?"))

year_remaining = 90 - age
day_remaining = year_remaining * 365
week_remaining = year_remaining * 52
month_remaining = year_remaining * 12

message = f'You have {day_remaining} days, you have {week_remaining} weeks, you have {month_remaining} months'
print(message)