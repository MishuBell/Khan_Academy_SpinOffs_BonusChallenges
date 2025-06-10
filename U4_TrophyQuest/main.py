import tql

tql.welcome_user()
user_name = tql.ask_for_username()

print(user_name + "?! " + tql.explain_quest_rules() + user_name + "?")
tql.ready_check()

times_table_choice = tql.ask_times_table()

result = tql.create_times_table_problem(times_table_choice)


# def game():
#     start()

#     while (running)

#     end()


