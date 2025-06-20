"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# 2. Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia",
}
print(CODE_TO_NAME)

# 4. Write a loop that prints all the states and names neatly lined up with string formatting
for code, name in CODE_TO_NAME.items():
    print(f"{code:3} is {name:20}")


