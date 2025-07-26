"""
CP1404 Practical
UnreliableCar class
"""

import random

from car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that is unreliable."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

