"""
CP1404 Practical
SilverServiceTaxi class test code
"""

from silver_service_taxi import SilverServiceTaxi
from sys import float_info


def main():
    """Test SilverServiceTaxi class."""
    my_taxi = SilverServiceTaxi("Hummer", 200, 2)
    my_taxi.drive(18)

