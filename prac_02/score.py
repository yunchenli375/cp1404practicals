# Refactor using a function to check the score

"""Score grading program that determines the grade based on the score input."""

import random


def main():
    """Main function to run the score grading program."""
    score = float(input("Enter score: "))
    print(determine_grade(score))
    randomized_score = random.randint(0, 100)
    print(f"random number is：{randomized_score:.2f}")
    print(determine_grade(randomized_score))


