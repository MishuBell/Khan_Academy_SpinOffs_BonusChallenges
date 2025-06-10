import random
# I have to start over. 

# Start with the core-game loop:
# Ask user to answer a question - incremement a counter for correct
# repeat question for incorrect

def main():
    # Variables
    correct_answer = 0
    user_table_choice = int(get_user_input())
    rand_num = random.randint(2,12)

    # ask users name

    while correct_answer < 10:
        
        result = generate_times_table_problem(user_table_choice, rand_num)
        print("What is " + str(user_table_choice) + " times " + str(rand_num))
        user_answer = get_user_input()
        # save result
        if int(user_answer) == result:
            correct_answer += 1
            rand_num = random.randint(2,9)
        else:
            print("Try again")



def get_user_input():
    user_input = input()
    return user_input 
    

def generate_times_table_problem(user_input, rand_num):
    result = user_input * rand_num
    return result

main()