import random, sys, itertools, time

# shuffled deck with values
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
          '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
suit = [chr(9829), chr(9827), chr(9830), chr(9824)]

deck = list(itertools.product(suit, list(values.keys())))
random.shuffle(deck)

def draw_card():
    return deck.pop()

def calculate_score(hand):
    score = 0
    for card in hand:
        if card == 'blank':
            continue
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

    for card in hand:

        if card == 'blank':
            rows[0] += '┌─────────┐'
            rows[1] += '|#####    |'
            rows[2] += '|  #####  | '
            rows[3] += '|    #####|'
            rows[4] += '└─────────┘'
            break
        else:
            suit, rank = card

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

def make_bet(income):

    while True:
        try:
            bet = int(input(f"You have {income}\nHow much would you like to bet: ").strip())

            if bet > income:
                print("Bet exceeds the amount you have, try again")

            else:
                return bet

        except ValueError:
            print("please only enter an integer")

def exit():
    while True:
        action = input("Press 'Y' to keep playing or 'Q' quit: ").strip().upper()

        if action == 'Y':
            return

        elif action == 'Q':
            print("Thanks for playing!!")
            sys.exit()

        else:
            print("Please only press 'Y' or 'Q'")


def main():
    money = 5000

    while True:
        bet = make_bet(money)

        player_hand = [draw_card(), draw_card()]
        dealer_hand = [draw_card(), 'blank']

        print(f"\nYour Hand: {calculate_score(player_hand)} ")
        display_cards(player_hand)

        time.sleep(2)
        print(f"\nDealer's Hand: {calculate_score(dealer_hand)} ")
        display_cards(dealer_hand)

        dealer_hand.pop()
        dealer_hand.append(draw_card())

        while True:
            player_turn(player_hand)

            if player_action == "hit":

                print("Your New Hand...  ")
                time.sleep(1)
                display_cards(player_hand)

                if calculate_score(player_hand) > 21:
                    print("Your score is over 21, you have lost\n\n")
                    break

            elif player_action == "stand":
                break

        if calculate_score(player_hand) > 21:
            money -= bet
            continue

        print("Dealer's reveals hand... ")
        time.sleep(1)
        display_cards(dealer_hand)


        dealer_turn(dealer_hand, calculate_score(dealer_hand))
        print("Dealer's final hand... ")
        time.sleep(2)
        display_cards(dealer_hand)


        if calculate_score(dealer_hand) > 21:
            print("The Dealer has bust, you win!!")
            money += bet
        elif calculate_score(player_hand) < calculate_score(dealer_hand):
            print("The Dealer has scored higher, you lose")
            money -= bet
        elif calculate_score(player_hand) == calculate_score(dealer_hand):
            print("The player and dealer have the same score, neither win")
        else:
            print("The player has scored higher, you win")
            money += bet
        print("\n\n")

        exit()


if __name__ == "__main__":
    main()