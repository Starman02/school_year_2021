"""Write a program that asks the user to enter the monthly costs for the following expenses incurred from operating his or her automobile: loan payment, insurance, gas, and maintenance. The program should then display the total monthly cost of these expenses, and the total annual cost of these expenses.

Assign meaningful names to your functions and variables. Every function also needs a comment explaining what it does and what other function it works with."""

"""
main():
calls the other functions
main is traditionally used as the first function in a program to organize the flow of the program logic

monthly():
Gather information from the user
Accumulate the total in a local variable
Print the monthly costs on screen, formatted appropriately for money
Pass the monthly cost to Function 2

yearly(monthly_total):
Accepts a float parameter
Calculates yearly cost by multiplying the monthly cost by 12
Displays the yearly cost on screen, formatted appropriately for money
"""


def main():
    monthly()


def monthly():
    loan_Mcost = float(input("What is your monthly loan payment?: "))
    insurance_Mcost = float(input("What is your monthly Insurance payment?: "))
    gas_Mcost = float(input("What is your monthly Gas payment?: "))
    maintenence_Mcost = float(input("What is your monthly Maintenance payment?: "))
    totalCost = loan_Mcost + insurance_Mcost + gas_Mcost + maintenence_Mcost
    print("Your Monthly cost is: ", format(totalCost, ",.2f"))
    yearlyCost(totalCost)


def yearlyCost(cost):
    print(cost)
    yearly = cost * 12
    print("your yearly cost is: ", yearly)


main()
