import random
#TODO: Add flavourful texts, offload game logic into its own file
# add trophys (ranks) for every successfully solved problem
# add a progress bar

def main():
    
    user_table_choice = get_user_numeric_input()

    random_numbers = random.sample(range(2,13), 10)

    i = 0
    while i <= 10:    
        result = generate_times_table_problem(user_table_choice, random_numbers[i])

        print("What is " + str(user_table_choice) + " times " + str(random_numbers[i]) + "?")

        if handle_input(get_user_input()) == result:
            i = i + 1
            continue
        else:
            print("Try again")


# Helpers
def get_user_numeric_input():
    user_input = handle_input(get_user_input())
    if user_input < 1 or user_input > 13:
        print("No cheating!")
        return get_user_numeric_input()
    else:
        return user_input

def handle_input(num):
    if num.isdigit():
        return int(num)
    else:
        return ord(num[0])

def get_user_input():
    user_input = input()
    return user_input 

def generate_times_table_problem(user_input, rand_num):
    return user_input * rand_num

main()