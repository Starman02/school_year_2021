# Word Jumble Game: guess the word made by the jumbled letters
import random


# main program logic
def jumble():
    # create a list of possible answers
    possible = ['blue', 'red', 'green', 'brown', 'yellow']

    # set the "category" to give the user a hint
    category = "colors"

    # welcome message
    print("Welcome to word jumble!")
    print("Try to guess the word -- category is", category, ".\n")

    # randomly select one of the answers for this game
    answer = random.choice(possible)

    # put the letters from the answer into a list
    letters = list(answer)

    # scramble the letters
    shuffle(letters)

    # display the scrambled letters with spaces between them
    for letter in letters:
        print(letter, end=" ")

    # get the user's guess  --  strip whitespace and make it lowercase
    guess = input("\nYour guess: ").strip().lower()
    # did they get it right?
    if answer == guess:
        print("\n yay you did it")
    else:
        print("wrong")


# this function randomly shuffles the values in the given list
def shuffle(some_list):
    # step through each subscript in the list
    # and swap it with a randomly chosen new subscript
    for index in range(len(some_list)):
        #  first, choose a random index value
        new_position = random.randrange(0, len(some_list))
        # if the random position is the same as the current index, get a different random value
        while new_position == index:
            new_position= random.randrange(0, len(some_list))
        (some_list[index], some_list[new_position]) = (some_list[new_position], some_list[index])
        # print(index, new_position, some_list)     # debugging statement -- shows how it works


# add this function to play again
def main():
    again = "y"
    while again[:1] != "n":
        jumble()
        again = input("Play again? (y/n) [y]").strip().lower()
    print("Thanks for playing!")


# start the game
jumble()
main()
