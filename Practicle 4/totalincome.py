__author__ = 'jc458537'
"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    incomes = []
    num_of_month = int(input("How many months? "))

    for month in range(1, num_of_month + 1):
        income = float(input("Enter income for month {}:".format(month)))
        incomes.append(income)

    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, num_of_month + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()
