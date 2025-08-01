"""
CP1404 Practical
SilverServiceTaxi class
"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that offers silver service."""

    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string representation of a SilverServiceTaxi."""
        return f"{super().__str__()}, plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + self.flagfall
