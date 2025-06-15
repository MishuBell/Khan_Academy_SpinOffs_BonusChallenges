import random

deck = ['apple', 'banana', 'orange', 'cherry', 'dragonfruit','prickly pear', 'golden kiwi', 'acerola', 'fruit fly swarm', 'deadly nightshade', 'blood orange', 'starfruit', 'peach leaf curl', 'penicillium fungi']

def main():
    rounds = 0
    max_rounds = 5
    user_score = 0
    npc_score = 0
    print(welcome_user())

    while rounds < max_rounds:
        linebreak(2)
        rounds_progress(rounds, max_rounds)
        print(f"Your overall: {user_score}")
        print(f"NPC overall: {npc_score}")
        # Player
        hand = build_hand()
        
        hand = discard_cards(hand, True)
        user_hand_score = evaluate_hand(hand)
        # Endplayer


        # NPC
        npc_hand = build_hand()

        npc_hand = discard_cards(npc_hand, False)
        npc_hand_score = evaluate_hand(npc_hand)
        # Endnpc

        # Totals
        user_score += user_hand_score
        npc_score += npc_hand_score
        # Endtotals


        print(display_hand_score(hand, True))
        print(display_hand_score(npc_hand, False))
        if user_hand_score > npc_hand_score:
            print("You've won the round!")
        elif npc_hand_score > user_hand_score:
            print("NPC won the round.")
        else:
            print("Its a draw!")
            rounds -= 1
        rounds += 1
    
    if max_rounds == 5:
        linebreak(2)
        if user_score > npc_score:
            print(f"You total {user_score} against their {npc_score}")
            print("You've won the game!!!!")
            print("Thank you for playing!!")
        elif npc_score > user_score:
            print(f"NPC totals {npc_score} against your {user_score}")
            print("NPC won the game ):")
            print("Thank you for playing!!")

        else:
            print("No one won the game. Its a draw")
            print("Thank you for playing!!")

# Helpers
def build_hand():
    hand = []
    # Fill hand with 6 cards
    for i in range(0, 6):
        rand_pick = random.randint(0, len(deck)-1)
        hand.append(deck[rand_pick])
    return hand

def discard_cards(hand, player):
    """
    Allows the player or NPC to discard cards from their hand until only 4 remain.

    Parameters:
        hand (list): The list of cards currently in the hand.
        player (bool): True if the user is discarding, False if the NPC is discarding.

    Returns:
        list: The updated hand after discarding cards.
    """
    # print(hand) 
    if player == True:
        while len(hand) >= 5:
            display_hand(hand)
            print(display_hand_score(hand, True))
            index = int(input("Discard:"))
            linebreak(1)
            if index < 1 or index > len(hand):
                print("The card you chose is out of index!")
                return discard_cards(hand, player)
            hand.pop(index - 1)
    else:
        while len(hand) >= 5:
            index = random.randint(1, len(hand))
            hand.pop(index - 1)
    return hand

def evaluate_hand(hand):
    """
    Calculates the total score for a hand of cards.

    Parameters:
        hand (list): A list of card names (str) in the hand.

    Returns:
        int: The total score for the hand.
    """
    score = 0
    for card in hand:
        score += evaluate_card(card)
    return score

def evaluate_card(card):
    """
    Returns a score value for a single card based on its name.
    (Values are placeholders for demonstration.)

    Parameters:
        card (str): The name of the card to evaluate.

    Returns:
        int: The score associated with the card.
    """
    if card == "apple":
        score = 1
    elif card == "banana":
        score = 2
    elif card == "orange":
        score = 3
    elif card == "cherry":
        score = 4
    elif card == "dragonfruit":
        score = -2
    elif card == "prickly pear":
        score = 5
    elif card == "golden kiwi":
        score = -3
    elif card == "acerola":
        score = 2
    elif card == "fruit fly swarm":
        score = -4
    elif card == "deadly nightshade":
        score = 3
    elif card == "blood orange":
        score = -1
    elif card == "starfruit":
        score = 4
    elif card == "peach leaf curl":
        score = -2
    elif card == "penicillium fungi":
        score = 3
    else:
        score = 0
    return score

def welcome_user():
    welcome_text = '''
Welcome! In this game, you will be given 6 cards to your hand,
of which you choose two to be discarded. Each card has different effects that add or subtract to your score.
'''
    return welcome_text

def rounds_progress(round, max_rounds):
    """
    Displays a progress bar indicating the current round out of the total rounds.

    Parameters:
        current_round (int): The current round number (starting from 1).
        max_rounds (int): The total number of rounds in the game.

    Returns:
        None
    """
    filled = '#' * round
    empty = '-' * (max_rounds - round)
    print( f"Round: [{filled}{empty}]")  

def display_hand(hand):
    """
    Displays the cards of the given hand.

    Parameters:
        hand (list): The list of cards in a given hand.
    Returns:
        None
    """
    for i in range(len(hand)):
        print(str(i + 1) + ": " + hand[i])


def display_hand_score(hand, player):
    """
    Returns the total score of the given hand.

    Parameters:
        hand (list): The list of cards in a given hand.
        player (bool): True if the hand belongs to the user, False for NPC.

    Returns:
        The score text
    """
    score_text = ""
    if player == True:
        score_text = "Your hand is valued at: " + str(evaluate_hand(hand))
    else:
        score_text = "The NPC hand is valued at: " + str(evaluate_hand(hand))
    return score_text

def linebreak(number):
    '''
    Prints a specified number of linebreaks
    '''
    for linebreak in range(number):
        print()

main()