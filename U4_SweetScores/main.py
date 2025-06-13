import random

user_hand = []
npc_hand = []
deck = ['apple', 'apple', 'apple', 'apple', 'apple','apple', 'apple', 'apple', 'apple', 'apple']
user_points = 0
npc_points = 0

def main():

    # Build hand for User
    # Build hand for NPC

    # Prompt user to discard two cards
    # Evaluate remaining cards to a score

    # Discard two NPC cards
    # Evaluate to cards to score

    # Compare scores

    # Repeat 5 times until a winner is chosen
    
    ## Add EXPLAIN function to give the user a definition of the cards effects

    pass


# Helpers
def build_hand():
    # Fill hand with 6 cards
    for i in range(0, 6):
        rand_pick = random.randint(1,6)
        user_hand.append(deck[rand_pick])
        print(user_hand)
    return user_hand



build_hand()