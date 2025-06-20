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

state_code = input("Enter short state: ")
while state_code != "":
    # 3. Change the program so lowercase inputs also work to show the state names
    state_code = state_code.upper()
    # 5. Change this to use exceptions and the "Easier to Ask Forgiveness than Permission" (EAFP) approach
    try:
        print(state_code, "is", CODE_TO_NAME[state_code])
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ")
