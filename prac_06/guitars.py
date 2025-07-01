"""
CP1404 Practical
guitar program
"""

from guitar import Guitar


def main():
    """program entrypoint"""
    print("My guitars!")
    guitars = collect_guitars_from_user_input()
    print("These are my guitars:")
    print_guitars_as_table(guitars)


def print_guitars_as_table(guitars: list[Guitar]):
    """print all guitar information like a table"""
    longest_name_length = 0
    longest_price_length = 0
    for guitar in guitars:
        longest_name_length = max(longest_name_length, len(guitar.name))
        longest_price_length = max(longest_price_length, len(f"{guitar.cost:,.2f}"))
    for i, guitar in enumerate(guitars, 1):
        print(
            f"Guitar {i}: {guitar.name:>{longest_name_length}}, worth $ {guitar.cost:>{longest_price_length},.2f} {'(vintage)' if guitar.is_vintage() else ''}"
        )


def collect_guitars_from_user_input():
    """returns a list of Guitar instances from interactive prompt input"""
    guitars = []
    new_guitar = create_guitar_from_user_input()
    while new_guitar is not None:
        guitars.append(new_guitar)
        print(f"{new_guitar} added.")
        new_guitar = create_guitar_from_user_input()
    return guitars


