from random import *
from itertools import *
from sys import *

# shuffled deck with values
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
          '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
suit = [chr(9829), chr(9827), chr(9830), chr(9824)]

deck = list(product(suit, list(values.keys())))
shuffle(deck)

def draw_card():
    return deck.pop()

def calculate_score(hand):
    score = 0
    for card in hand:
        score += values[card[1]]
    return score

def player_turn(hand):
    global player_action
    while True:
        player_action = input("Would you like to 'hit' or 'stand': ").strip().lower()

        if player_action == "hit":
            hand.append(draw_card())
            break
        elif player_action == "stand":
            break
        else:
            print("please type 'hit' or 'stand' only")

    return

def dealer_turn(hand, score):
    while score < 17:
        hand.append(draw_card())
        score = calculate_score(hand)

    return hand

def display_cards(hand):
    rows = ['', '', '', '', '']

    for suit, rank  in hand:

        if rank == '10':
            space = ''
        else:
            space = ' '

        rows[0] += '┌─────────┐  '
        rows[1] += f'| {rank}{space}      |  '
        rows[2] += f'|    {suit}    |  '
        rows[3] += f'|      {space}{rank} |  '
        rows[4] += '└─────────┘  '

    for row in rows:
        print(row)

    return

def main():
    player_hand = [draw_card(), draw_card()]
    dealer_hand = [draw_card(), draw_card()]

    print("Your Hand: ")
    for card in player_hand:
        print(f"{card[1]} of {card[0]}")
    print(f"Your Score: {calculate_score(player_hand)}")

    print("Dealer's Hand: ")
    print(f"{dealer_hand[0][1]} of {dealer_hand[0][0]}")
    print("'Unknown'")
    print(f"Dealer Score: {values[dealer_hand[0][1]]}")

    while True:
        player_turn(player_hand)

        if player_action == "hit":

            print("Your Hand: ")
            for card in player_hand:
                print(f"{card[1]} of {card[0]}")
            print(f"Your Score: {calculate_score(player_hand)}")

            if calculate_score(player_hand) > 21:
                print("Your score is over 21, you have lost")
                exit()

        elif player_action == "stand":
            break

    print("Dealer's Hand: ")
    for card in dealer_hand:
        print(f"{card[1]} of {card[0]}")
    print(f"Dealer's Score: {calculate_score(dealer_hand)}")

    dealer_turn(dealer_hand, calculate_score(dealer_hand))
    print("Dealer's Final Hand:")
    for card in dealer_hand:
        print(f"{card[1]} of {card[0]}")
    print(f"Dealer's Final Score: {calculate_score(dealer_hand)}")

    if calculate_score(dealer_hand) > 21:
        print("The Dealer has bust, you win!!")
        exit()

    elif calculate_score(player_hand) < calculate_score(dealer_hand):
        print("The Dealer has scored higher, you lose")

    elif calculate_score(player_hand) == calculate_score(dealer_hand):
        print("The player and dealer have the same score, neither win")

    else:
        print("The player has scored higher, you win")



if __name__ == "__main__":
    main()