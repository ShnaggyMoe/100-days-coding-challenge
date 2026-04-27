# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
bids = {}

while True:
    print("\n" * 20)
    name = input('What is your name?')
    bid = input('What is your bid?')
    more_bid = input("Are there any other bidders? Type 'yes' or 'no'.")
    bids[name] = int(bid)
    if more_bid == 'no':
        break
winner = max(bids, key=lambda x: bids[x])

print(f"The winner is {winner} with a bid of {bids[winner]}")