import random
import TQ

# Hello Player. This is TrophyQuest - a spin-off of the Trophy case bonus challenge.
# Instead of earning badges for participation, i tried to let the player journey through ranks by answering multiplication challenges correctly.
# I hope you enjoy!


def main():
    TQ.welcome_user()
    user_name = TQ.explain_quest_rules(TQ.ask_for_username())
    TQ.ready_check()

    print('''Which times table will you master?
[   Enter a number from 2 to 12   ]:''')

    user_table_choice = TQ.get_user_numeric_input()
    random_numbers = random.sample(range(2,13), 10)


    i = 0
    while i < 10:
        print()
        TQ.ranks(i, user_name)

        result = TQ.generate_times_table_problem(user_table_choice, random_numbers[i])

        print("What is " + str(user_table_choice) + " times " + str(random_numbers[i]) + "?")

        if TQ.handle_input(TQ.get_user_input()) == result:
            i = i + 1
            if i == 10:
                TQ.success()
            continue
            
        else:
            TQ.print_negation()
            TQ.linebreak(1)


main()