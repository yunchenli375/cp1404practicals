"""
CP1404 Practical
Estimated time: 15 minutes
Actual time: 38 minutes
"""

# We want to get the current year
# Hard-coding the current year as a constant may not be considered as the best practice
import datetime


class Guitar:
    """Represent a Guitar object."""

    VINTAGE_THRESHOLD_YEARS = 50

    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar object.

        name: str, the name of the guitar
        year: int, the year of the guitar
        cost: float, the cost of the guitar"""
        self.name = name
        self.year = year
        self.cost = cost
