MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}


def resource_check(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def insert_coins(coffee_type):
    print("\nEnter the coins....")
    quarters = float(input("Enter number of quarters: "))
    dimes = float(input("Enter number of dimes: "))
    nickles = float(input("Enter number of nickles: "))
    pennies = float(input("Enter number of pennies: "))
    amount_cost = (quarters*0.25)+(dimes*0.10)+(nickles*0.05)+(pennies*0.01)
    if amount_cost >= MENU[coffee_type]["cost"]:
        balance_amt = amount_cost - MENU[coffee_type]["cost"]
        return balance_amt
    else:
        return -1


def make_coffee(coffee_type):
    resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
    resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
    if coffee_type != "espresso":
        resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]


while True:
    user_response = input("What would you like? (espresso/latte/cappuccino): ")
    if user_response == "report":
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}gm')
        money_amt = "{:.2f}".format(resources["money"])
        print(f'Money: ${money_amt}')
    elif user_response == "latte" or user_response == "espresso" or user_response == "cappuccino":
        drink = MENU[user_response]
        if resource_check(drink["ingredients"]):
            amount = insert_coins(user_response)
            if amount == -1:
                print("Sorry that's not enough money. Money refunded.")
            elif amount >= 0.0:
                if amount != 0.0:
                    resources["money"] += MENU[user_response]["cost"]
                    amount = "{:.2f}".format(amount)
                    print(f"Here is ${amount} dollars in change")
                make_coffee(user_response)
                print(f"Here is your {user_response}")
    elif user_response == "off":
        break
