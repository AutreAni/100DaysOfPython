from data import MENU, resources, coins


coffee_types = MENU.keys()
should_continue = True


def print_report():
    print("Reporting...")
    for key in resources:
        print(f"{key.capitalize()}: {resources[key]}")


# TODO 5. Process coins.
def process_money():
    total_coins = {}
    total_sum = 0
    for key in coins:
        money = input(f"How many {key}: ").lower()
        total_coins[key] = int(money)
    for key in total_coins:
        total_sum += coins[key] * total_coins[key]
    total_sum = round(total_sum, 2)
    return total_sum


def update_resources(coffee_type):
    spent_resources = {
        "money": -MENU[coffee_type]["cost"]
    }
    for key in MENU[coffee_type]["ingredients"]:
        spent_resources[key] = MENU[coffee_type]["ingredients"][key]

    for key in spent_resources:
        resources[key] = resources[key] - spent_resources[key]


# TODO 7. Make Coffee.
def make_coffee(coffee_type):
    has_resources = check_resources(coffee_type)
    if has_resources:
        cost = MENU[coffee_type]["cost"]
        print(f"{coffee_type} costs {cost}$. Please, insert your coins.")
        money = process_money()
        print(f"Money inserted: ${money}")
        # TODO 6. Check transaction successful?
        if money < cost:
            print(f"It is not enough money, here is your refund: ${money}")
        else:
            if money > cost:
                change = round(money - cost, 2)
                print(f"Here is your change: {change}$")
            update_resources(coffee_type)
            print(f"Here is your {coffee_type}, enjoy!")
            print_report()


# TODO 4. Check resources sufficient?
def check_resources(coffee_type):
    required_resource = MENU[coffee_type]["ingredients"]
    insufficient = []
    for ingredient in required_resource:
        if required_resource[ingredient] > resources[ingredient]:
            insufficient.append(ingredient)
    if len(insufficient):
        print(f'Sorry there is not enough {", ".join(insufficient)}')
        return False
    else:
        return True


while should_continue:
    # TODO 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
    user_choice = input(" What would you like? (espresso/latte/cappuccino/report): ").lower()
    # TODO 3. Print report.
    if user_choice == "report":
        print_report()
    elif user_choice in coffee_types:
        make_coffee(user_choice)
    # TODO 2.Turn off the Coffee Machine by entering “ off ” to the prompt.
    elif user_choice == "off":
        should_continue = False
        print("Turning off!")
    else:
        print("Invalid answer, choose something from the list")


# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “ Sorry there is not enough water. ”
# c. The same should happen if another resource is depleted, e.g. milk or coffee

# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

# a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “ Sorry that's not enough money. Money refunded. ”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
# places.

# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink.
