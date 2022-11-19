from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

mr_coffee = CoffeeMaker()
mr_menu = Menu()
mr_money = MoneyMachine()

machine_is_on = True


def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    return


while machine_is_on:
    clear_screen()
    prompt = input("What would you like? espresso/latte/cappuccino\n")
    match prompt.lower():
        case "off":
            machine_is_on = False
        case "report":
            mr_coffee.report()
        case "espresso" | "latte" | "cappuccino":
            drink = mr_menu.find_drink(prompt.lower())
            if mr_coffee.is_resource_sufficient(drink):
                if mr_money.make_payment(drink.cost):
                    mr_coffee.make_coffee(drink)
        case _:
            continue
