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

# showing the player info 
    def display_turn_info(): 
        
        # shows whos playing 
        player_name = f"Player {turn + 1}"
        my_hand = player_hands[turn]
        print(f"\n {player_name}'s turn!")
        print(f"Top Card: [{top_card}] (Color: {current_color})")
        print("Your Hand:") 
        
        # shows the players hand 
        for i, card in enumerate(my_hand):
            print(f"  {i + 1}: [{card}]")

    # handles the players taking turns 
    def handle_turn(): 
        
        # being able to change the variables 
        nonlocal turn, winner, top_card, current_color
        
        # checking turns 
        my_hand = player_hands[turn]
        player_name = f"Player {turn + 1}"
        
        # the card play
        choice = input("Play a card (by number) or 'draw': ").lower()

# using uno rules to play for each turn 
        if choice == 'draw':
            drawn_card = deck.pop()
            my_hand.append(drawn_card)
            print(f"{player_name} drew [{drawn_card}]. Turn over.")
            turn = (turn + 1) % 2
            return # end this turn

        try: 
            # get the actual card from the hand 
            choice_index = int(choice) - 1
            card_they_played = my_hand[choice_index]
            
            # using the can pplay card function 
            # if the card can be played 
            if can_play_card(card_they_played, top_card, current_color):
                
                # play the card
                top_card = my_hand.pop(choice_index)
                discard_pile.append(top_card)
                print(f"{player_name} plays [{top_card}]")

                # check for win 
                if not my_hand:
                    winner = player_name
                    return # end the turn (and the game)
                
                if len(my_hand) == 1:
                    print(f"!!!! {player_name} shouts UNO")
                
                # handle wild color
                if "Wild" in card_they_played:
                    color_choices = ["Red", "Green", "Blue", "Yellow"]
                    while True:
                        # let the player choose the card they want to pick 
                        c_choice = input("Pick a color (1-4 for R,G,B,Y): ")
                        if c_choice in ['1','2','3','4']: 
                            
                            # getting the position of the current_color of the card being played 
                            current_color = color_choices[int(c_choice) - 1]
                            print(f"{player_name} chose {current_color}!")
                            break
                else: 
                      # if the card is a normal card then checks the colour 
                    current_color = card_they_played.split(" ")[0]
                    
                # apply effects for taking turns 
                opponent_turn = (turn + 1) % 2
                opponent_hand = player_hands[opponent_turn]
                opponent_name = f"Player {opponent_turn + 1}"
                skip_turn = False

                # check the actions for each turn 
                if "Skip" in card_they_played or "Reverse" in card_they_played:
                    print(f" {opponent_name} gets skipped")
                    skip_turn = True
                elif "Draw 2" in card_they_played:
                    print(f" {opponent_name} draws 2 and is skipped")
                    opponent_hand.extend([deck.pop() for _ in range(2)])
                    skip_turn = True
                elif "Draw 4" in card_they_played:
                    print(f" {opponent_name} draws 4 and is skipped")
                    opponent_hand.extend([deck.pop() for _ in range(4)])
                    skip_turn = True
                    
                # set next turny_played:
                    print(f" {opponent_name} draws 2 and is skipped")
                    opponent_hand.extend([deck.pop() for _ in range(2)])
                    skip_turn = True
                elif "Draw 4" in card_they_played:
                    print(f" {opponent_name} draws 4 and is skipped")
                    opponent_hand.extend([deck.pop() for _ in range(4)])
                    skip_turn = True
                    
                # set next turny_played:
                    print(f" {opponent_name} draws 4 and is skipped")
                    opponent_hand.extend([deck.pop() for _ in range(4)])
                    skip_turn = True
                    
                # set next turn
                if not skip_turn:
                    turn = (turn + 1) % 2
                # if skip turn is true, turn just stays the same
                
                # error validation 
            else:
                print(" Can't play that ... Try again")
        
        # validation 
        except (ValueError, IndexError):
            print("Not a real choice ... Pick a number or draw")

    # if there isnt a winner yet 
    while winner is None:
        
        check_and_reshuffle() 
        display_turn_info() 
        handle_turn() 
        
    # game over
    print(f"\n GAME OVER ")
    print(f" {winner} WINS ")

# run the game
if __name__ == "__main__":
    play_game()
