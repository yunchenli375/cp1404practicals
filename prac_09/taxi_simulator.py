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

    def menu(self):
        """returns a valid menu choice"""
        print(self.MENU)
        choice = input(">>> ")
        while choice == "" or choice.upper()[0] not in self.CHOICE:
            print("Invalid option")
            print(f"Bill to date: ${self.fare:.2f}")
            print(self.MENU)
            choice = input(">>> ")
        return choice.upper()[0]

    def drive(self):
        """attempt to drive the current taxi"""
        if self.current_idx == -1:
            print("You need to choose a taxi before you can drive")
        else:
            distance = input("Drive how far? ")
            while not distance.isdigit() or int(distance) < 0:
                print("Invalid distance")
                distance = input("Drive how far? ")
            distance = int(distance)
            # if the start_fare method returns the taxi object itself,
            # we can chain the method calls!
            self.taxis[self.current_idx].start_fare()
            self.taxis[self.current_idx].drive(distance)
            trip_fare = self.taxis[self.current_idx].get_fare()
            print(
                f"Your {self.taxis[self.current_idx].name} trip cost you ${trip_fare:.2f}"
            )
            self.fare += trip_fare
        print(f"Bill to date: ${self.fare:.2f}")

