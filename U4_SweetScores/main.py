import random
#TODO: Sanitize Inputs

deck = ['kiwi', 'apple', 'apple', 'orange', 'banana','apple', 'fruit fly', 'poison apple', 'banana', 'cherry']

def main():
    rounds = 0
    max_rounds = 5

    print(welcome_user())
    while rounds < max_rounds:
        rounds_progress(rounds, max_rounds)

        hand = build_hand()
        display_hand_score(hand)
        hand = discard_cards(hand, True)
        display_hand_score(hand)
        user_score = evaluate_hand(hand)
        display_hand_score(hand)
        # User Score

        npc_hand = build_hand()
        npc_hand = discard_cards(npc_hand, False)
        npc_score = evaluate_hand(npc_hand)
        # NPC Score

        if user_score > npc_score:
            print("You've won the round!")
        else:
            print("NPC won the round.")

        rounds += 1

# Helpers
def build_hand():
    hand = []
    # Fill hand with 6 cards
    for i in range(0, 6):
        rand_pick = random.randint(1,6)
        hand.append(deck[rand_pick])
    return hand

def discard_cards(hand, player):
    
    # print(hand) 
    if player == True:
        while len(hand) >= 5:
            # print discard instruction
            display_hand(hand)
            index = int(input())
            hand.pop(index - 1)
    else:
        while len(hand) >= 5:
            index = random.randint(1, len(hand))
            hand.pop(index - 1)
            # DEBUG ONLY: Print NPC hand
    return hand

def evaluate_hand(hand):
    score = 0
    for card in hand:
        score += evaluate_card(card)
    return score

def evaluate_card(card):
    score = 0
    if card == "apple":
        score += 1
    elif card == "kiwi":
        score += 2
    elif card == "orange":
        score += 3
    elif card == "fruit fly":
        score -= 2
    elif card == "poison apple":
        score -= 1
    elif card == "cherry":
        score +=1
    return score

def welcome_user():
    welcome_text = '''
Welcome! In this game, you will be given 6 cards to your hand,
of which you choose two to be discarded. Each card has different effects that add or subtract to your score.
But watch out! Some cards have special effects!
'''
    return welcome_text

def rounds_progress(round, max_rounds):
    filled = '#' * round
    empty = '-' * (max_rounds - round)
    print( f"Round: [{filled}{empty}]")  

def display_hand(hand):
    for i in range(len(hand)):
        print(str(i + 1) + ": " + hand[i])

def display_hand_score(hand):
    print("Your hand is valued at: " + str(evaluate_hand(hand)))

main()