# Sentinel values, Accumulators, and Data Validation are tools you will use often

# *************************************************************************************************************
# A Sentinel value is a special value used to trigger the end of a loop
# Sentinel values are often used when getting multiple input values from the keyboard

# When getting data from the user, clue them in about the sentinel value you are looking for
# the sentinel value must be a value that will not be valid data for the situation

# sentinel value for this loop is 0
in_value = int(input("\nENTER A NUMBER (0 to quit): "))
while in_value != 0:
    print(in_value, "times five is", in_value * 5)
    # don't forget to get the next value
    in_value = int(input("\nENTER A NUMBER (0 to quit): "))

# *************************************************************************************************************
# An Accumulator is a variable used to hold a running total
# before you use the accumulator, make sure it is set to the correct initial value, usually zero

# initialize accumulator
total = 0
# if calculating an average, I also need to count the values, so I need a second accumulator
count = 0
# since 0 is a valid test score, use -1 as the sentinel value
in_value = int(input("\nENTER test score (-1 to end): "))
while in_value != -1:
    # add this score to the total and add one to the count of scores
    total += in_value
    count += 1
    # get the next value
    in_value = int(input("\nENTER test score (-1 to end): "))

# calculate the average once all values have been entered (outside of the loop)
# NOTE: if no values were entered, the count is zero and division by zero will generate an error
average = total / count
print("\nFor", count, "Scores, the average is", average)

# *************************************************************************************************************
# A Data Validation loop tests for a valid input value and, if invalid,
#     repeatedly requests a new value until a valid value is entered.

# prompt the user to enter a valid choice
choice = input("\nChoose and option, (A, B, or C)")
# for this example, assume the user needs to enter an uppercase response
# the while loop should test for BAD data so that good data will cause the loop to exit
while choice != 'A' and choice != 'B' and choice != 'C':
    # since bad data was found, give an error and prompt again
    choice = input("\nERROR, INVALID DATA, PLEASE ENTER A B or C")

# the data validation loop only exits once good data has been received
print("You selected", choice)
