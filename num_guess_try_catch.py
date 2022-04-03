#!/usr/bin/env python3
# Created By: Ferdous Sediqi
# Date: March 23, 2022
# This program asks the user for a random number 0-9
# then if check if they guessed it right or wrong
# and tell them the right number if they were wrong.
# also check using try and except to see if the user
# input is an integer or a string

# import math random
import random


def main():
    # set random number between 0-9
    random_number = random.randint(0, 9)
    print("")
    string_input = input("Enter a number 0-9 ")
    # check the guess number as well as input type
    try:
        integer_input = int(string_input)
        print("")
        print("you entered an interger")
        if integer_input == random_number:
            print("You guessed it right!")
        else:
            # display the right number if they guessed it wrong
            print("You guessed the wrong number.")
            print("")
            print("The right number was ", random_number)
    except Exception:
        print("")
        print(string_input, "is not an integer.")
        print("The right number was ", random_number)


if __name__ == "__main__":
    main()
