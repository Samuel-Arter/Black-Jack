from random import *
from itertools import *

# shuffled deck with values
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
          '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
suit = [chr(9829), chr(9827), chr(9830), chr(9824)]

deck = list(product(suit, list(values.keys())))
shuffle(deck)

# player/dealer score
player_score = 0
dealer_score = 0

def draw_card():
    return deck.pop()

def calculate_score(hand, score):
    for card in hand:
        score += values[card[1]]
    return score

def player_turn(hand):
    while True:
        action = input("Would you like to 'hit' or 'stand': ").strip().lower()

        if action == "hit":
            hand.append(draw_card())
            break
        elif action == "stand":
            break
        else:
            print("please type 'hit' or stand' only")

    return



def main():
    player_hand = [draw_card(), draw_card()]
    dealer_hand = [draw_card(), draw_card()]

    print(f"Your hand: {player_hand[0][1]} of {player_hand[0][0]}\n "
          f"          {player_hand[1][1]} of {player_hand[1][0]}")
    print(f"Your Score: {calculate_score(player_hand, player_score)}")

    player_turn(player_hand)



if __name__ == "__main__":
    main()