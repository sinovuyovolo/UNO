import random

COLORS = ["Red", "Blue", "Green", "Yellow"]
ACTIONS = ["Reverse", "Skip", "Draw 2"]
WILD_ACTIONS = ["Wild", "Wild Draw 4"]

def create_deck():
    deck = [] #an empty deck for each time we reshuffle the cards we draw and play should be put in it

    for color in COLORS:
        for num in range(10):
            card =  f"{color} {num}"
            deck.append(card)
            if num != 0:
                deck.append(card)
