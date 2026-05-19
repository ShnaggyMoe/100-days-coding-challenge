from importlib.resources import is_resource

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

shop_menu = Menu()
coffee_machine = CoffeeMaker()
piggy_bank = MoneyMachine()

while True:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == 'off':
        break
    elif user_choice == "report":
        coffee_machine.report()
        piggy_bank.report()
    else:
        drink = shop_menu.find_drink(user_choice)
        can_make = coffee_machine.is_resource_sufficient(drink)
        if can_make == True:
            order = drink.cost
            rich = piggy_bank.make_payment(order)
            if rich == True:
                coffee_machine.make_coffee(drink)