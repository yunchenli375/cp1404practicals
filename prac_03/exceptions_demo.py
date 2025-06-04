"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When failed to convert the input to an integer.

2. When will a ZeroDivisionError occur?
When the denominator input is number 0.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Add a check to ensure the denominator is not zero before performing the division.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")