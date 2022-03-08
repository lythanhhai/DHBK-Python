from Coffee_maker import CoffeeMaker
from Menu import Menu, MenuItem
from Money_machine import MoneyMachine

is_on = True 
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while is_on:
    your_choice = input("What do you enter: ")
    # tạo đối tương
    if your_choice == "off":
        is_on = False
        break
    if your_choice == "report":
        coffee_maker.report()
    elif your_choice == "process":
        money_machine.process_coins()
    elif your_choice == "report_money":
        money_machine.report()
    else:
        order_item = menu.find_drink(your_choice)
        if coffee_maker.is_resource_sufficient(order_item):
            if money_machine.make_payment(order_item.cost):
                coffee_maker.make_coffee(order_item)