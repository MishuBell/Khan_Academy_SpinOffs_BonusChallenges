import random
#TODO: Sanitize Inputs

hand = []
npc_hand = []
deck = ['kiwi', 'apple', 'apple', 'orange', 'banana','apple', 'fruit fly', 'poison apple', 'banana', 'cherry']
user_points = 0
npc_points = 0

def main():
    
    hand = build_hand()
    hand = discard_cards(hand)
    print(evaluate_hand(hand))
    pass



# Helpers
def build_hand():
    # Fill hand with 6 cards
    for i in range(0, 6):
        rand_pick = random.randint(1,6)
        hand.append(deck[rand_pick])
    return hand

def discard_cards(hand):

    # Show hand
    print(hand) 

    while len(hand) >= 5:
        print("Discard a card by entering a valid number! \n")
        print("Type a num:")
        index = int(input())
        hand.pop(index - 1)
    return hand

def evaluate_hand(hand):
    score = 0
    for card in hand:
        score += evaluate_card(card)
        print(card)
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

main()