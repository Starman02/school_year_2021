"""
hen, write a program that reads the contents of the two files into two separate lists. The user should be able to enter
a boy's name or a girl's name. The application should check both lists, and then display messages indicating whether
the names were among the most popular if the name was on one of the lists or that the name was not on the lists of popular names.
"""


def main():
    listcreator()


def gosearcher(largelist):  # sorts big list for the designated name
    confirmedState = False
    target = str(input('Enter a name: ')).capitalize()      # makes it capitalized
    for i in largelist:
        if str(i) == target:
            confirmedState = True
            break
        else:
            confirmedState = False
    if confirmedState:
        print(target, "Is a popular name")
    else:
        print(target, 'is not a popular name')


def listcreator():
    # puts all boy names in a list
    boylist = []
    boyFile = open('BoyNames.txt')
    for line in boyFile:  # reads all names in guyfile
        boylist.append(line.rstrip('\n'))

    boyFile.close()
    # puts all girl names in a list
    girlList = []
    girlFile = open('GirlNames.txt')
    for line2 in girlFile:  # reads all names in guyfile
        girlList.append(line2.rstrip('\n'))

    bigList = boylist + girlList
    gosearcher(bigList)


main()
