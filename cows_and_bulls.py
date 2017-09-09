#!/usr/bin/python3
#
#
__author__ = 'bofh'

import random, string, re

#------------------------------------------------------------------------------

def num_input(f_string = "\nEnter a 4-digit number: "):
    f_num = input(f_string)

    if f_num == "q":
        quit()

    while (not re.match(r'^\d+$', f_num) or (int(f_num) < 1000 or int(f_num) > 9999)):
        f_num = input("\nEnter a 4-digit number: ")
        print()

    return f_num

def game_loop():
    f_debug = 0
    f_attempts = 1
    f_initial_string = "\nWelcome to Cows and Bulls game.\nEnter a 4-digit number: "
    
    f_cows_and_bulls = str(random.randint(1000, 9999))
    f_num = num_input(f_initial_string)

    if (f_num != f_cows_and_bulls):
        while (f_num != f_cows_and_bulls):    
            f_cows = 0
            f_bulls = 0
            f_cows_position = []
            f_bulls_position = []

            if f_debug == 1:
                print(f_cows_and_bulls)

            for i in range(len(f_cows_and_bulls)):
                if (f_num[i] == f_cows_and_bulls[i]):
                    f_bulls += 1
                    f_bulls_position.append(i)

            if f_debug == 1:
                print("Bulls", f_bulls_position)

            for i in range(len(f_cows_and_bulls)):

                if f_debug == 1:
                    print("i-bulls", i, f_num[i])

                if (i not in f_bulls_position):
                    for j in range(len(f_cows_and_bulls)):

                        if f_debug == 1:
                            print("j-bulls", j, f_cows_and_bulls[j])

                        if (j not in f_bulls_position):
                            if (f_num[i] == f_cows_and_bulls[j]):
                                f_cows += 1
                                f_cows_position.append(i)
                                break

                if f_debug == 1:
                    print("Cows", f_cows_position)

            if (f_cows < 2):
                f_cows_str = "cow,"
            else:
                f_cows_str = "cows,"
            if (f_bulls < 2):
                f_bulls_str = "bull."
            else:
                f_bulls_str = "bulls."

            print(f_cows, f_cows_str, f_bulls, f_bulls_str)
            f_attempts += 1
            f_num = num_input()
        print("\nYou guessed in", f_attempts, "attempts.\n")
    else:
        print("\nYou guessed in one attempt!\n")

#------------------------------------------------------------------------------

if __name__ == "__main__":
    game_loop()
