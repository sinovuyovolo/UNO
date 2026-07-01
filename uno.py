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

    for color in COLORS:
        for action in ACTIONS:
            card = f"{color} {action}"

            deck.append(card)
            deck.append(card)
    for _ in range(4):
        deck.append("Wild")
        deck.append(card)

    random.shuffle(deck)
    return deck

def can_play_card(card, top_card, current_color):

     # checks if the card is wild and returns true 
     if "Wild" in card:
        return True
     
     # if we have a normal card, we split the colour and the number of the card
     card_color, card_value = card.split(" ", 1)

      # checks the card colour we split with colour being played and if true it returns true 
     if card_color == current_color:
        return True
     
    # this also checks the card but using the value of the card 
    # if true returns true or else false 

     top_parts = top_card.split(" ", 1)
     top_value = top_parts[1] if len(top_parts) > 1 else top_parts[0]
     if card_value == top_value:
         return True
     
     return False #if not true it should return False