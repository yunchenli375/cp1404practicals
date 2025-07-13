"""
CP1404 Practical
testing of guitar.py
"""

from guitar import Guitar
import datetime

GIBSON_L5_CES_YEAR = 1922
GIBSON_L5_CES_COST = 16035.4
ANOTHER_GUITAR_YEAR = 2013


def main():
    """program entrypoint"""
    current_year = datetime.date.today().year
    gibson = Guitar("Gibson L-5 CES", GIBSON_L5_CES_YEAR, GIBSON_L5_CES_COST)
    another = Guitar("Another Guitar", ANOTHER_GUITAR_YEAR)
    print(
        f"{gibson.name} get_age() - Expected {current_year - GIBSON_L5_CES_YEAR}. Got {gibson.get_age()}"
    )
    print(
        f"{another.name} get_age() - Expected {current_year - ANOTHER_GUITAR_YEAR}. Got {another.get_age()}"
    )
    print(
        f"{gibson.name} is_vintage() - Expected {current_year - GIBSON_L5_CES_YEAR >= Guitar.VINTAGE_THRESHOLD_YEARS}. Got {gibson.is_vintage()}"
    )
    print(
        f"{another.name} is_vintage() - Expected {current_year - ANOTHER_GUITAR_YEAR >= Guitar.VINTAGE_THRESHOLD_YEARS}. Got {another.is_vintage()}"
    )


main()
