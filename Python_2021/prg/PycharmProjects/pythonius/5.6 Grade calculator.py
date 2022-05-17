"""
Write a program that asks a user to enter five test scores. You will need to create five variables to hold these scores.
The purpose of this assignment is to get practice passing information between functions, this is not a good example of the way programs are really written,
but it will help you to understand how to pass parameters. Follow the program logic shown.

main -
asks the user for each of the five test scores, stores them in separate variables (score1, score2, etc)
calls calc_average and passes the five variables, storing the result in a variable
average = calc_average(score1, score2, score....
calls determine_grade, passing it the average variable, storing the result in a variable
prints the letter grade

calc_average -
This function should accept the five test scores as arguments
returns the average of the scores.

determine_grade -
This function should accept the average of the test scores as an argument
returns a letter grade based on the following scale:

"""


def main():  # assigns variables and calls average
    score1 = float(input("Enter Test score: "))
    score2 = float(input("Enter Test score: "))
    score3 = float(input("Enter Test score: "))
    score4 = float(input("Enter Test score: "))
    score5 = float(input("Enter Test score: "))
    average = calc_average(score1, score2, score3, score4, score5)
    print("The average of all the test scores is: ", average)
    determine_grade(average)  # sends info to determinator


def calc_average(score01, score02, score03, score04, score05):
    average = (score01 + score02 + score03 + score04 + score05) / 5  # PEMDAS IS KEY
    return average


def determine_grade(jomba):  # sorts grade
    if jomba >= 90:
        print("you have a final grade of an A")
    elif jomba >= 80:
        print("You have a final grade of an B")
    elif jomba >= 70:
        print("You have a final grade of an C")
    elif jomba >= 60:
        print("your have a final grade of an D")
    elif jomba < 60:
        print("Your final grade is an F")
    else:
        print("Error not in graderange")  # if a unwanted value is detected, it sends it out


main()  # start main
