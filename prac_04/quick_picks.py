"""
CP1404/CP5632 Practical
Quick Pick Lottery Ticket Generator
"""

import random

LINE_LENGTH = 6
MIN = 1
MAX = 45


def main():
    picks = int(input("How many quick picks? "))
    for i in range(picks):
        quick_pick = unique_sampling()
        quick_pick.sort()
        print(" ".join(f"{number:2}" for number in quick_pick))


def unique_sampling():
    """return a list containing LINE_LENGTH unique random numbers between MIN and MAX."""
    result = []
    while len(result) < LINE_LENGTH:
        number = random.randint(MIN, MAX)
        if number not in result:
            result.append(number)
    return result


main()
