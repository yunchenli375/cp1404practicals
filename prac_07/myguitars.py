"""
CP1404 Practical
Guitar client program
"""

from guitar import Guitar
import csv


def main():
    """program entrypoint"""
    guitars = []
    with open("guitars.csv", "r") as in_file:
        guitars = create_guitar_list_from_csv_file(in_file)
        for guitar in sorted(guitars):
            print(guitar)

    for new_guitar in collect_guitars_from_user_input():
        guitars.append(new_guitar)

    with open("guitars.csv", "w") as out_file:
        for guitar in guitars:
            out_file.write(guitar.dump_as_csv() + "\n")


def create_guitar_list_from_csv_file(in_file):
    """create a list of Guitar objects from a CSV file object"""
    guitars = []
    reader = csv.reader(in_file)
    for row in reader:
        guitars.append(Guitar(row[0], int(row[1]), float(row[2])))
    return guitars


def collect_guitars_from_user_input():
    """returns a list of Guitar instances from interactive prompt input"""
    guitars = []
    new_guitar = create_guitar_from_user_input()
    while new_guitar is not None:
        guitars.append(new_guitar)
        print(f"{new_guitar} added.")
        new_guitar = create_guitar_from_user_input()
    return guitars


def create_guitar_from_user_input():
    """returns a Guitar instance from interactive prompt input"""
    name = input("Name: ")
    if name == "":
        return None
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitar = Guitar(name, year, cost)
    return guitar


main()