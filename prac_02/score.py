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


def determine_grade(score):
    """Determine the grade based on the score."""
    if score >= 50:
        if score >= 90:
            if score > 100:
                return "Invalid score"
            else:
                return "Excellent"
        else:
            return "Passable"
    elif score < 0:
        return "Invalid score"
    else:
        return "Bad"

def ddetermine_grade(randomized_score):
    """Determine the grade based on the score."""
    if randomized_score >= 50:
        if randomized_score >= 90:
            return "Excellent"
        else:
            return "Passable"
    else:
        return "Bad"


main()
