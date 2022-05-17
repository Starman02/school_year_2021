"""
Write a program that reads the numbers.txt file – it contains a series of integers. Your program will calculate the average of all
of the numbers stored in the file and display the total on the screen. Format to show a maximum of two digits to the right of
the decimal point.

Use appropriate variables, functions, and comments.
"""


def main():
    averageReader()


def averageReader():
    count = 0
    number = open("numbers.txt", "r")  # opens file
    memory = 0.0
    for line in number:  # for every number in file do:
        amount = float(line)  # sets/resets amount to next value
        memory += amount  # stores values to add again
        count += 1  # the way logic is set up, program counts 2 numbers at a time, so count must increase by 2 every time
    average = memory / count
    print("There were ", count, " numbers")
    print("\nThe total of all the numbers was: ", format(memory, ","))
    print("\nThe average of all numbers was", format(average, ".2f"))
    number.close()


main()
