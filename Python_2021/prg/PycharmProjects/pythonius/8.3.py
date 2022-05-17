"""
Write a program that lets the user enter a string and displays the letter that appears most frequently in the string. Ignore spaces, punctuation, and uppercase vs lowercase.



Get a phrase from the user
Convert the phrase to lowercase (or uppercase -- it just needs to be consistent)
Loop through the characters in the phrase and create a list to hold its unique
letters
....(in other words, skip over non-alphabetic characters and letters already in the
list, only add unique letters)
Create a list of the same size as the unique letter list to hold counts and
initialize to zeros
Loop through the unique letter list using subscript values
Create an inner loop that loops through the characters in the original string
....if the character in the original string matches the letter in the unique list
.........then add one to the count list at the corresponding subscript
When both loops have completed, find the maximum value in the count list -- this is
the highest count
Fetch the corresponding letter from the unique list -- this is the letter with the
highest count
Display the results
'''
"""


def main():
    phrase = str(input("Enter a phrase"))
    mainPhrase = phrase.upper()  # makes the mainphrase uppercase
    conversion(mainPhrase)

    # sends organized string off to get sorted


def conversion(ring):  # converts all letters in string into a sorted list
    string1 = ring.replace(" ", "")  # removes all white spaces
    noNumeric = ''.join([i for i in string1 if not i.isdigit()])  # removes all non alphabetical values
    list1 = []
    list1[:0] = noNumeric
    list1.sort()
    blankList = []
    for x in list1:  # assigns unique values from list1 into blanklist
        if x not in blankList:
            blankList.append(x)

    countList = [0] * len(blankList)  # list to hold all highest letters

    for item in blankList:
        # move to next spot

        del countList[-1]  # removes extra end created by insert
        repeating_count = 0  # resetes counting value

        for letters in list1:

            if item == letters:
                repeating_count += 1  # add to spot in list
        countList.insert(blankList.index(item), repeating_count)

    largestValue1 = blankList[max(countList)]
    largestValue = blankList[max(countList) + 1]
    try:
        if largestValue == largestValue1:
            mainvalue = largestValue
            print("The most frequently appearing letter is: ", mainvalue)
        else:
            print("The two most frequently appearing letter(s) are: ", largestValue, largestValue1)
    except IndexError:
        print("To many common letters, number is over 3")


main()
