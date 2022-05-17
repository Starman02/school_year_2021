"""
Have a function that creates a list of 20 random integers between 1 and 100 (Assign them dynamically, store the list in a variable.)
Have a function get a number from the user that is between 1 and 100 (validate to ensure a number between 1 and 100 was entered instead of text or something out of range using a try and except statement).
Pass both the list and the user's number to a function and have it display all numbers in the list that is greater than the user's number. If there are not any, display a message that explains there are no numbers in the list greater than the entered number.

"""
import random


def megamain():
    numberAsking()


def main(asked, randomed):
    print(randomed)                     # sorts items and makes sure the numbers are greater than
    truthseek = False # make this true once i> is found
    try:
        indexcounter = asked
        randomed.index(indexcounter)  #
        for i in randomed:
            if i > asked:
                print('You guessed a number right')
    except ValueError:  # if no values are found it auto starts the number asker
        print("Number not found, recounting")
        numberAsking()


def randomGenerator(temp):  # generates the random numbers and list, also stores tempoary variable to send up
    randomList = []
    for a in range(20):  # assigns a random variable 20 times
        randomNums = random.randrange(1, 100)
        randomList.append(randomNums)

    main(temp, randomList)


def numberAsking():
    try:  # catches string errors
        request = int(input("Enter a value of 1 through 100"))
        while request > 1 or request < 100:
            randomGenerator(request)
    except ValueError:
        print("\nInvalid Data type, please enter valid data")  # catches value errors and restarts function

        # starts random generator and sends data to the generator to store it


megamain()
