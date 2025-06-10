import random

def get_user_numeric_input():
    user_input = handle_input(get_user_input())
    if user_input < 2 or user_input > 12:
        print_warning()
        linebreak(1)
        return get_user_numeric_input()
    else:
        print_affirm()
        linebreak(1)
        return user_input

def handle_input(num):
    '''
    Converts user input to an integer if possible
    If the input is a digit, returns it as an int
    If not, returns the Unicode code point of the first character
    Arguments:
        num (str): The user input string to process
    Returns:
        int: The integer value of the input or the Unicode code point of the first character
    '''
    if num.isdigit():
        return int(num)
    else:
        return ord(num[0])

def get_user_input():
    user_input = input("You: ")
    return user_input 

def generate_times_table_problem(user_input, rand_num):
    return user_input * rand_num

def print_warning():
    '''
    Prints a random warning string
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

def linebreak(number):
    '''
    Prints a specified number of linebreaks
    '''
    for linebreak in range(number):
        print()

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

def print_negation():
    '''
    Prints a random denial string.
    Example: 'Try again!', 'Close!!", or 'Almost had it!'
    '''

    rand_num = random.randint(1,7)
    denial = ""

    if rand_num == 1:
        denial = "Try again!"
    elif rand_num == 2:
        denial = "Close!"
    elif rand_num == 3:
        denial = "Almost!"
    elif rand_num == 4:
        denial = "Think again!"
    elif rand_num == 5:
        denial = "One more try!"
    elif rand_num == 6:
        denial = "Not quite!"
    else:
        denial = "Are you sure?"
    print(denial)
    pass

def welcome_user():
    welcome_message = '''Hello apprentice! 🧙
Are you ready to embark on a journey to become a powerful math-magus today?'''
    print(welcome_message)
    print_prompt()
    linebreak(1)
    get_user_input()
    print_affirm()
    linebreak(1)

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

def ask_for_username():
    ask_username = "What is your name, mighty apprentice?"
    print(ask_username)
    user_name = get_user_input()
    print_affirm()
    linebreak(1)
    return user_name

def explain_quest_rules(user_name):
    '''
    Prints the quest introduction and rules, addressing the user by name
    Arguments:
        user_name (str): The player's name to personalize the quest message
    '''

    explain_rules =  f"{user_name}?! A truly formidable apprentice. Let me explain your quest ... \n\
You must choose a multiplication table (2-12). Answer 10 multiplication facts correctly, and you shall ascend to the rank of Numerus Magus, master of Multiplication! (This comes with bragging rights!) \n\
Are you prepared to begin your quest, {user_name}?"
    print(explain_rules)
    return user_name

def ready_check():
    print_prompt()
    linebreak(1)
    get_user_input()
    print_affirm()
    linebreak(1)

def ranks(i, user_name):
    '''
    Prints the player's rank title based on their progress
    Arguments:
        i (int): The current progress value
        user_name (str): The player's name to include in the rank title
    '''
    if i == 1:
        print(f"[ {user_name} the Numerical Novice ]")
    elif i == 2:
        print(f"[ {user_name} the Equation Evoker ]")
    elif i == 3:
        print(f"[ {user_name} the Multiplication Maverick ]")
    elif i == 4:
        print(f"[ {user_name} the Factor Fighter ]")
    elif i == 5:
        print(f"[ {user_name} the Theorem Tactician ]")
    elif i == 6:
        print(f"[ {user_name} the Arithmancer ]")
    elif i == 7:
        print(f"[ {user_name} the Polynomial Paladin ]")
    elif i == 8:
        print(f"[ {user_name} the Algebraic Archmage ]")
    elif i == 9:
        print(f"[ {user_name} the The Prime Oracle ]")
    elif i == 10:
        print(f"[ {user_name} the Numerus Magus! ]")

def success():
    success_message = "By the power of prime numbers and the wisdom of equations, you have conquered the trials of multiplication. Your name shall be inscribed in the great Codex of Calculation, where only the most formidable minds dwell.\n"
    thank_you_message ="Thank you for playing this game! Sincerely! I wish you all the best of progress and joy going forward in this course 🖤"

    print(success_message)
    print(thank_you_message)