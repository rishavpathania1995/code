# simple guessing game

import random

cpu_num =  random.randint(1,10)
State = True

while State:
    user_input = int(input(
        "please gusses he no from 1 to 10 :"))
    if user_input==cpu_num :
        print(
            "user wins")

    else:
        print(
            f"computer wins:{cpu_num}")

    con_input = input(
        "please enter 'y ' to continue")                         

    if con_input != 'y':
        State = False
