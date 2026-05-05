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
}

money_in_machine = 0

def check_resources(choice):
    for item in MENU[choice]["ingredients"]:
        if resources[item] < MENU[choice]["ingredients"][item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def make_coffee(choice):
    for item in MENU[choice]["ingredients"]:
        resources[item] -= MENU[choice]["ingredients"][item]

def process_coins():
    quarter = int(input("Insert your payment.\n"
                     "Quarters: ")) * 0.25
    dime = int(input("Dimes: ")) * 0.1
    nickel = int(input("Nickels: ")) * 0.05
    penny = int(input("Pennies: ")) * 0.01
    money = round((quarter + dime + nickel + penny), 2)
    return money

def check_transaction(money, cost):
    global money_in_machine
    if money == cost:
        money_in_machine += money
        return True
    elif money > cost:
        change = money - cost
        print(f"Here is your change: ${change}")
        money_in_machine += cost
        return True
    elif money < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False

while True:
    choice = input('What would you like? ').lower()
    if choice == 'report':
        for key in resources:
            value = resources[key]
            print(f"{key}: {value}mg")
        print(f"Money: ${money_in_machine} ")
    elif choice == "off":
        break
    elif check_resources(choice) is True:
        cost = MENU[choice]["cost"]
        customer_money = process_coins()
        transaction_success = check_transaction(customer_money, cost)
        if transaction_success is True:
            make_coffee(choice)
            print(f"{choice} coming right up!")