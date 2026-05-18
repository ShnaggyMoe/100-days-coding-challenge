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
    "water": 30,
    "milk": 200,
    "coffee": 100,
}

money_in_machine = 0
while True:
    choice = input('What would you like? ').lower()
    if choice == 'espresso':
        if resources["water"] >= MENU["espresso"]["ingredients"]["water"]:
            if resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
                print("espresso coming up!")
            else:
                print("Sorry there is not enough coffee.")
        else:
            print("Sorry there is not enough water.")
    elif choice == 'latte':
        pass
    elif choice == 'cappuccino':
        pass
    elif choice == 'report':
        for key in resources:
            value = resources[key]
            print(f"{key}: {value}mg")
        print("debug")
        print(f"Money: ${money_in_machine} ")
    elif choice == "off":
        break