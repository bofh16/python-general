#!/usr/bin/python3
#
#
__author__ = 'bofh'

import re

#------------------------------------------------------------------------------

def num_input():
    f_num = input("\nEnter a number to check: ")
    while (not re.match(r'^\d+$', f_num)):
         num_to_input=input("\nEnter a NUMBER to check: ")

    return int(f_num)

#------------------------------------------------------------------------------

def print_result(f_is_prime, f_is_even, f_div):
    if f_is_prime:
        print("The number is prime.\n")
    elif f_is_even:
        print("The number is even, so can NOT be prime.\n")
    else:
        print("The number is NOT prime. The smalest dividor is " + str(f_div) + ".\n")

#------------------------------------------------------------------------------

def loop_prime(f_num_to_check):
    if (f_num_to_check % 2 == 0):
        f_is_prime = False
        f_is_even = True
        f_div = 0
    else :
        f_upper_range = int(f_num_to_check / 2 + 1)
        for i in range(2, f_upper_range):
            if (f_num_to_check % i == 0):
                f_is_prime = False
                f_is_even = False
                f_div = i
                break
        else:
            f_is_prime = True
            f_is_even = False
            f_div = 0

#    return f_is_prime, f_is_even, f_div

    print_result(f_is_prime, f_is_even, f_div)

# -----------------------------------------------------------------------------

if __name__ == "__main__":
    loop_prime(num_input())
