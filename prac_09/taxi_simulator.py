"""
CP1404 Practical
Taxi Simulator Program
"""


class TaxiSimulator:
    """Simulator for a taxi service."""

    MENU = "q)uit, c)hoose taxi, d)rive"
    CHOICE = "QCD"

    def __init__(self, taxis):
        """Initialise the simulator with no taxis."""
        self.taxis = taxis
        # instead of using a reference to the taxi object,
        # which looks like a copy in Python and may cause confusion,
        # we maintain an index of the current taxi
        self.current_idx = -1
        self.fare = 0.0

