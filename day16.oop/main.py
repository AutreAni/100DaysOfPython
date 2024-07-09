from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
should_continue = True
while should_continue:
    menu_list = menu.get_items()
    user_choice = input(f"What would you like? {menu_list}: ").lower()
    if user_choice == "report":
        coffee_maker.report()
    elif user_choice == "off":
        should_continue = False
        print("Turning off!")
    else:
        item = menu.find_drink(user_choice)
        if item:
            if coffee_maker.is_resource_sufficient(item):
                is_paid = money_machine.make_payment(item.cost)
                if is_paid:
                    coffee_maker.make_coffee(item)
                    coffee_maker.report()
