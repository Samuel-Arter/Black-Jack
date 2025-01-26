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

def dealer_turn(hand):
    while calculate_score(hand) < 17:
        hand.append(draw_card)

    return


def main():
    player_hand = [draw_card(), draw_card()]
    dealer_hand = [draw_card(), draw_card()]

    print("Your Hand: ")
    for card in player_hand:
        print(f"{card[1]} of {card[0]}")
    print(f"Your Score: {calculate_score(player_hand)}")

    print

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









if __name__ == "__main__":
    main()