"""
CP1404 Practical
Guitar client program
"""

from guitar import Guitar
import csv


def main():
    """program entrypoint"""
    with open("guitars.csv", "r") as in_file:
        guitars = create_guitar_list_from_csv_file(in_file)
        for guitar in sorted(guitars):
            print(guitar)


def create_guitar_list_from_csv_file(in_file):
    """create a list of Guitar objects from a CSV file object"""
    guitars = []
    reader = csv.reader(in_file)
    for row in reader:
        guitars.append(Guitar(row[0], int(row[1]), float(row[2])))
    return guitars


main()
