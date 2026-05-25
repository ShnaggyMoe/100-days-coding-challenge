menu = {
    "espresso" : {"water" : 50, "coffee" : 18, "cost" : 1.5},
    "latte" : {"water" : 200, "milk" : 150, "coffee" : 24, "cost" : 2.5},
    "cappuccino" : {"water" : 250, "milk" : 100, "coffee" : 24,
                    "cost" : 3,}

}

resources = {
    "water": 300, "milk": 200, "coffee": 100, "money": 0,
}

def counting_coins():
    quarters_inserted = int(input("How many quarters?"))
    dimes_inserted = int(input("How many dimes?"))
    nickles_inserted = int(input("How many nickles?"))
    pennies_inserted = int(input("How many pennies?"))
    quarter_change = quarters_inserted * 0.25
    dime_change = dimes_inserted * 0.1
    nickel_change = nickles_inserted * 0.05
    penny_change = pennies_inserted * 0.01
    total_coins_inserted = quarter_change + dime_change + nickel_change + penny_change
    return total_coins_inserted

def check_resources(user_choice):
    for item in menu[user_choice]:
        if menu[user_choice][item] < resources[item]:
            print(f"Sorry there's not enough {item}.")
    return