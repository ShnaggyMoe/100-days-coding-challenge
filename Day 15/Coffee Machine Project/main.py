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

while True:
    choice = input('What would you like? ').lower()
    if choice == 'espresso':
        something
    elif choice == 'latte':
        something
    elif choice == 'cappuccino':
        something
    elif choice == 'report':
        for key in resources:
            value = resources[key]
            print(f"{key}: {value}mg")
    elif choice == "off":
        break