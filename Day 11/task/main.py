import random
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

while True:
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_cards = []
    computer_cards = []
    player_cards.append(random.choice(cards))
    player_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))

    player_score = sum(player_cards)
    computer_score = sum(computer_cards)
    print(f"Your hand: {player_cards}, current score: {player_score} ")
    print(f"Computer's first card: {computer_cards[0]} ")
    player_choice = input("Type 'y' to get another card, type 'n' to pass: ")
    player_bust = False
    while True:
        if player_choice == 'y':
            player_cards.append(random.choice(cards))
            player_score = sum(player_cards)
            print(f"Your hand: {player_cards}, current score: {player_score} ")
            if player_score > 21:
                player_bust = True
                print(f"Computer's final hand: {computer_cards}, final score: {computer_score}\n"
                      "You went over. You lose!")
                break
            player_choice = input("Type 'y' to get another card, type 'n' to pass: ")
        else:
            break

    if not player_bust:
        while True:
            if computer_score < 17:
                computer_cards.append(random.choice(cards))
                computer_score = sum(computer_cards)
            else:
                break

        if player_score > computer_score:
            print(f"Your final hand: {player_cards}, final score: {player_score}\n "
                  f"Computer's final hand: {computer_cards}, final score: {computer_score} "
                  "Opponent went over. You win :D")
        elif computer_score > player_score:
            print(f"Your final hand: {player_cards}, final score: {player_score}\n "
                  f"Computer's final hand: {computer_cards}, final score: {computer_score} "
                  "You went over. You lose :( ")
        else:
            print(f"Your final hand: {player_cards}, final score: {player_score}\n "
                  f"Computer's final hand: {computer_cards}, final score: {computer_score} "
                  "Draw")
    play = input("Do you want to play again? Type 'y' or 'n': ").lower()
    if play == 'n':
        break