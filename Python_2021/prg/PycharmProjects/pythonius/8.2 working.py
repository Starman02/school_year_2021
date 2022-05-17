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
    phone_number = str(input("Enter a phone number you wish to convert, exclude one: "))
    phoneSplit = phone_number.split("-")
    # sort
    front = phoneSplit[0]
    front1 = front.upper()

    middle = phoneSplit[1]
    middle1 = middle.upper()
    back = phoneSplit[2]
    back1 = back.upper()
    testing(front1, middle1, back1)


def testing(first, second, third):
    alpha = ['0', '1', '2', 'A', 'B', 'C', '3', 'D', 'E', 'F', '4', 'G', 'H', 'I', '5', 'J', 'K', 'L', '6', 'M', 'N',
             'O', '7', 'P', 'Q', 'R', 'S', '8', 'T', 'U', 'V', '9', 'W', 'X', 'Y', 'Z', '-']

    digits = ['0', '1', '2', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4', '5', '5', '5', '5',
              '6', '6', '6', '6', '7', '7', '7', '7', '7', '8', '8', '8', '8', '9', '9', '9', '9', '9',
              '-']

    secondTranslate = ""
    firstTranslate = ""
    thirdTranslate = ""

    if first.isalpha():
        for number in first:
            for item in range(0, len(alpha)):
                if alpha[item] == number:
                    firstTranslate += digits[item]

    if second.isalpha():
        for number in second:
            for item in range(0, len(alpha)):

                if alpha[item] == number:
                    secondTranslate += digits[item]

    if third.isalpha():
        for number in third:
            for item in range(0, len(alpha)):
                if alpha[item] == number:
                    thirdTranslate += digits[item]

    finaltranslate1 = ""
    finaltranslate2 = ""
    finaltranslate3 = ""
    if firstTranslate == "":
        finaltranslate1 = first
    elif firstTranslate != "":
        finaltranslate1 = firstTranslate

    if secondTranslate == "":
        finaltranslate2 = second
    elif secondTranslate != "":
        finaltranslate2 = secondTranslate

    if thirdTranslate == "":
        finaltranslate3 = third
    elif thirdTranslate != "":
        finaltranslate3 = thirdTranslate

    print('Converted to: ', finaltranslate1, '-', finaltranslate2, '-', finaltranslate3)


main()
