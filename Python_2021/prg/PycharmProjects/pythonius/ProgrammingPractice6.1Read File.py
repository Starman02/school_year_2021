"""
Your Python file will:
Read and Display the list of names from the file
Display the number of names that are read from the file (You will need a variable to keep a count of the number of items read from the file.)

"""


def listOffNames():     # function
    count = 0
    nameData = open("names.txt")
    for line in nameData:
        print(line.strip())         # prints line and removes excess
        count += 1
    print("There were ", count, " names in file")
    nameData.close()


listOffNames()
