"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    num_months = int(input("How many months? "))

    for month in range(1, num_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print("\nIncome Report\n-------------")
    display_income_report(incomes)


def display_income_report(incomes):
    """Display a report of monthly incomes and cumulative total."""
    total = 0
    month = 1
    for monthly_income in incomes:
        total += monthly_income
        print(
            f"Month {month:2} - Income: ${monthly_income:10.2f} Total: ${total:10.2f}"
        )
        month += 1


main()
