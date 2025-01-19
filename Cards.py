from random import *
from itertools import *

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
        score +=


def main():
    player_hand = [draw_card(), draw_card()]
    return player_hand

if __name__ == "__main__":
    print(main())