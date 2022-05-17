"""
    This will demonstrate:
    1. using pseudocode to plan logic
    2. using nested if statements
    3. using known values to test results
"""

# PSEUDOCODE is English-like phrases or statements that
# describe the logical steps needed to solve a problem

# PROBLEM:
# A mobile phone service provider has three different subscription packages for its customers:
# Package A: For $39.99 per month 450 minutes are provided. Additional minutes are $0.45 per minute.
# Package B: For $59.99 per month 900 minutes are provided. Additional minutes are $0.40 per minute.
# Package C: For $69.99 per month unlimited minutes provided.

# Write a program that calculates a customer's monthly bill. It should ask which package
# the customer has purchased and how many minutes were used. It should then display the
# total amount due. Use a dollar sign and two decimal places for currency.

# Input validation: Be sure the user only selects package A, B, or C.
# Otherwise, display an appropriate error.

# PSEUDOCODE:

# What data is GIVEN?
# In a real-life program, this data may be read from a file or pulled from a database
#
packageA_rate = 39.99
packageA_additional_minutes = 0.45
packageA_provided_minutes = 450
packageB_rate = 59.99
packageB_additional_minutes = 0.40
packageB_provided_minutes = 900
packageC_rate = 69.99

# code logic
#
# get package from user (A, B, C)
# if package is A:
#   get minutes_used from user as an integer
#   if minutes_used are more than provided minutes:
#       set additional_cost to (minutes_used - provided minutes) * additional minute cost
#   else:
#       set additional_cost to zero
#   set total_cost to monthly package rate + additional_cost
#   display results with appropriate formatting
# or if package is B:
#   << logic the same as for package A but with package B rates >>
# or if package is C:
#   display the monthly rate for package C
# otherwise give an error

# example for testing package
package = input("Which package do you have? ")

if package == "A":          # does not test for lowercase
    print("using package A")
elif package == "B" or package == "b":      # correct way to test for both values
    print("using package B")
# Python reads this as elif (package == "C") or ("c")   --> anything non zero is True
elif package == "C" or "c":         # this will ALWAYS be True because "c" evaluates to True
    print("using package C")
else:                               # this else will never be reached
    print("invalid package")

# be sure to test your program with all possible combinations:
#    all packages, invalid package, with or without additional minutes
#    make sure calculated results are correct
