"""
CP1404 Practical
UnreliableCar class test code
"""

from unreliable_car import UnreliableCar


def main():
    my_unreliable_car = UnreliableCar("Unreliable", 100, 75)
    for i in range(30):
        my_unreliable_car.drive(5)
        print(my_unreliable_car)


main()
