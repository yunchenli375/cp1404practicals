"""
CP1404 Practical
Taxi class test code
"""

from taxi import Taxi


def main():
    """docstring"""
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)
    print(my_taxi)
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)


main()
