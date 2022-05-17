"""
t should handle any IOError exceptions that are raised when the file is opened and data is read from it.

"""


def main():
    averageReader()


def averageReader():
    count = 0
    memory = 0.0
    try:  # sees if file is avalible
        number = open("numbers2.txt", "r")  # opens file

        for line in number:  # for every number in file do:
            amount = float(line)  # sets/resets amount to next value
            memory += amount  # stores values to add again
            count += 1
    except FileNotFoundError:
        print("ERROR: FILE COULD NOT BE ACCESSED")
    except ValueError:
        print("ERROR, INVALID DATA TYPE: Stopping at last value")

    average = 0
    if count > 0:
        average = memory / count
    else:
        print("program ended in an error")
    print("There were ", count, " numbers")
    print("\nThe total of all the numbers was: ", format(memory, ","))
    print("\nThe average of all numbers was", format(average, ".2f"))


main()
