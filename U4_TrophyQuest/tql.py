import random


# Functions
def welcome_user():
    welcome_message = '''Hello apprentice! 🧙
Are you ready to embark on a journey to become a powerful math-magus today?'''
    print(welcome_message)
    print_prompt()
    linebreak(1)
    get_user_input()
    print_affirm()
    linebreak(1)

def ask_for_username():
    ask_username = "What is your name, mighty apprentice?"
    print(ask_username)
    user_name = get_user_input()
    print_affirm()
    linebreak(1)
    return user_name

def explain_quest_rules():
    explain_rules = '''A truly formidable apprentice. Let me explain your quest ... \n
You must choose a multiplication table. Answer 10 multiplication facts correctly, and you shall ascend to the rank of Numerus Magus, master of Multiplication! (This comes with bragging rights!)

Are you prepared to begin your quest, '''
    return explain_rules

def ready_check():
    print_prompt()
    linebreak(1)
    get_user_input()
    print_affirm()
    linebreak(1)

# Main game loop
def ask_times_table():
    times_table_prompt = '''Which times table will you master?
[   Enter a number from 2 to 9   ]:'''
    print(times_table_prompt)

    users_table_choice = validate_input(get_user_input())

    if users_table_choice <2 or users_table_choice >9:
        print_warning()
        linebreak(1)
        ask_times_table()
    else:
        print_affirm()
        print("You chose the " + str(users_table_choice) + " times table.")
        linebreak(1)
    return int(users_table_choice)

def main_game_loop(times_table):
    

    pass

def experience_bar():
    print("[----------]")

# Helpers
def create_times_table_problem(user_value):
    rand_num = random.randint(2,9)

    result = user_value * rand_num
    print("What is " + str(user_value) + " times " + str(rand_num) + " ?")
    while validate_input(get_user_input()) != result:
        print("Try again!")
        


def validate_input(users_table_choice):
    if users_table_choice.isdigit():
        return int(users_table_choice)
    else:
        return ord(users_table_choice[0])

def print_warning():
    '''
    Prints a random warning string.
    Example: 'Awesome!', 'Great!", or 'Marvellous!'
    '''

    rand_num = random.randint(1,7)
    affirm = ""

    if rand_num == 1:
        affirm = "Please adhere to the rules!"
    elif rand_num == 2:
        affirm = "No cheating!"
    elif rand_num == 3:
        affirm = "Nuh-uh!"
    elif rand_num == 4:
        affirm = "You shall not pass!"
    elif rand_num == 5:
        affirm = "No foul play!"
    elif rand_num == 6:
        affirm = "No trickery, apprentice!"
    else:
        affirm = "Do not!"
    print(affirm)

def get_user_input():
    return input("You: ")

def print_prompt():
    '''
    Prints a random affirmation prompt string for user confirmation.
    Example: '[   Yes / Absolutely   ]: '
    '''

    rand_num = random.randint(1,5)
    prompt = ""

    if rand_num == 1:
        prompt = "[   Yes / Absolutely!   ]"
    elif rand_num == 2:
        prompt = "[   Yes / Indeed!   ]"
    elif rand_num == 3:
        prompt = "[   Yes / Of course!  ]"
    elif rand_num == 4:
        prompt = "[   Yes / Always!   ]"
    else:
        prompt = "[   Yes / Verily!   ]"
    print(prompt)

def print_affirm():
    '''
    Prints a random positive affirmation string.
    Example: 'Awesome!', 'Great!", or 'Marvellous!'
    '''

    rand_num = random.randint(1,7)
    affirm = ""

    if rand_num == 1:
        affirm = "Magnificent!"
    elif rand_num == 2:
        affirm = "Splendiferous!"
    elif rand_num == 3:
        affirm = "Most excellent!"
    elif rand_num == 4:
        affirm = "Prodigious!"
    elif rand_num == 5:
        affirm = "By the stars, wondrous!"
    elif rand_num == 6:
        affirm = "Verily, a triumph!"
    else:
        affirm = "Resplendent!"
    print(affirm)

def linebreak(number):
    '''
    Prints a specified number of linebreaks.
    '''
    for linebreak in range(number):
        print()
