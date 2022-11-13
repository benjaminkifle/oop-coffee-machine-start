from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


while is_on:
    drink_choice = input(f" What would you like? ({menu.get_items()}): ").lower()
    if drink_choice == "off":
        is_on = False
    elif drink_choice == "report":
        coffee_maker.report(), money_machine.report()
    else:
        drink = menu.find_drink(drink_choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
