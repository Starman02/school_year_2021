"""
Write a program that gets a string from the user containing a person's first, middle, and last names and then displays their
first, middle, and last initials.  (Creating a new variable and concatenating each letter plus a '.' is the easiest way to do this.)


"""


def main():
    try:
        name = str(input("Please enter your first, middle, and last name (Seperated by spaces)"))
        sifting(name)
    except IndexError:
        print("Invalid name or format")


def sifting(name):
    split_names = name.split(" ")  # splits name into a 1d list
    first_name = str(split_names[0])  # assigns first name to the list item inside split names
    first_letter = first_name[0]  # assisns first letter to the first letter of first name

    middle_name = str(split_names[1])  # does what first name and first letter do but for the second item
    second_letter = middle_name[0]

    last_name = str(split_names[2])  # gatheres last names first letter
    last_letter = last_name[0]

    print(first_letter.upper(), second_letter.upper(), last_letter.upper())


main()
