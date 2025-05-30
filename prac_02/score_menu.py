# Add score_menu program

MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    """Main function to run the score menu program."""
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_grade(score))
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell.")


def validate_score(score_string):
    """Validate the score string to ensure it is a digit and within the range 0-100."""
    if score_string.isdigit():
        score = int(score_string)
        if determine_grade(score) != "Invalid score":
            return True
        else:
            return False
    else:
        return False


def get_valid_score():
    """Prompt the user for a valid score and return it as an integer."""
    score_string = input("Enter score: ")
    valid = validate_score(score_string)
    while not valid:
        print("Invalid score")
        score_string = input("Enter score: ")
        valid = validate_score(score_string)
    return int(score_string)



