
"""
Many companies use telephone numbers like 555-GET-FOOD so the number is easier for their customers to
remember. On a standard telephone the alphabetic letters are mapped to numbers in the following fashion:
A, B, C = 2

D, E, F = 3

G, H, I = 4

J, K, L = 5

M, N, O = 6

P, Q, R, S = 7

T,U, V, = 8

W, X, Y, Z = 9

Write a program that asks the user to enter a 10-character telephone number in the format XXX-XXX-XXXX. The
application should display the telephone number with any alphabetic characters that appeared in the original
translated to their numeric equivalent.
"""


def main():
    splitANDsort()


def splitANDsort():
    # split
    phone_number = str(input("Enter a phone number you wish to convert: "))
    phoneSplit = phone_number.split("-")
    # sort
    front = ""
    back = ""
    middle = ""
    if phoneSplit[0] == 1:
        extra = phoneSplit[0]
        front = phoneSplit[1]
        middle = phoneSplit[2]
        back = phoneSplit[3]
    elif phoneSplit[0] != 1:
        extra = 1
        front = phoneSplit[0]
        middle = phoneSplit[1]
        back = phoneSplit[2]
    testing(front, middle, back)


def testing(first, second, third):
    first_test = False
    second_test = False
    third_test = False
    if first.isalpha():
        first_test = True
        print(first_test)

    if second.isalpha():
        second_test = True
        print(second_test)

    if third.isalpha():
        third_test = True
        print(third_test)

    alpha = ['0', '1', '2', 'A', 'B', 'C', '3', 'D', 'E', 'F', '4', 'G', 'H', 'I', '5', 'J', 'K', 'L', '6', 'M',
                 'N',
                 'O', '7', 'P', 'Q', 'R', 'S', '8', 'T', 'U', 'V', '9', 'W', 'X', 'Y', 'Z', '-']

    digits = ['0', '1', '2', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4', '5', '5', '5', '5',
                  '6', '6', '6', '6', '7', '7', '7', '7', '7', '8', '8', '8', '8', '9', '9', '9', '9', '9',
                  '-']
    secondTranslate = ""
    firstTranslate = ""
    thirdTranslate = ""
    if first_test:
        for number in first:
            for item in range(0, len(digits)):
                if number == digits[item]:
                    firstTranslate += alpha[item]

    if second_test == True:
        for number in second:
            for item in range(0, len(digits)):
                 if number == digits[item]:
                    secondTranslate += alpha[item]

    if third_test == True:
         for number in second:
            for item in range(0, len(digits)):
                if number == digits[item]:
                    thirdTranslate += alpha[item]

    print(first, second, third)


main()
