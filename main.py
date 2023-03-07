from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
maker = CoffeeMaker()
money = MoneyMachine()
is_on = True
while is_on:
    choice = input(f"What would you like to have({menu.get_items()}):")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        maker.report()
        money.report()
    else:
        drink = menu.find_drink(choice)
        if maker.is_resource_sufficient(drink):
            cost = money.make_payment(drink.cost)
            if cost:
                maker.make_coffee(drink)

