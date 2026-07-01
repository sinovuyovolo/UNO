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

# function for setting up the game 
def play_game(): 
    # we create the deck using the function we made 
    deck = create_deck()
    
    # we then create the players will play 
    # each player must have 7 cards
    player_hands = [ [deck.pop() for _ in range(7)],[deck.pop() for _ in range(7)] ]
    
    # creating a list for the cards that will be played 
    discard_pile = []
    
    # you get the card from top of the deck and it becomes your top card 
    top_card = deck.pop()
     
     # checks if you drew a draw 4 
     # if it is you draw a new card 
    while "Draw 4" in top_card:
        deck.append(top_card); random.shuffle(deck); top_card = deck.pop()
        
        # since the card is now legal we put it down
    discard_pile.append(top_card)
    
    # the colour that is being played currently 
    current_color = random.choice(COLORS) if "Wild" in top_card else top_card.split(" ")[0]
    turn = 0
    winner = None

   # a function to check and reshuffle 
    def check_and_reshuffle(): 
    
    # check if the deck has less cards
        if len(deck) < 5:
            print("Deck is low. Reshuffling ") 
            # saves the top card 
            top_card_save = discard_pile.pop() 
            
            # adds back the pile and shuffles it 
            deck.extend(discard_pile)
            random.shuffle(deck) 
            
            # cleans the pile
            discard_pile.clear()
            discard_pile.append(top_card_save)
