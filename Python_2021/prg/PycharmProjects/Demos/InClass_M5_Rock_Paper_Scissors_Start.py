# write a program that plays ROCK, PAPER, SCISSORS against the computer
# 1. When the program begins, it should generate a random number in the range of 1 to 3
#       where 1=ROCK, 2=PAPER, 3=SCISSORS
# 2. The user enters a choice of "rock", "paper" or "scissors" at the keyboard
# 3. The computer's choice is displayed
# 4. The winner is determined and the result is displayed: ROCK > SCISSORS > PAPER > ROCK
# If both players choose the same value, play again
import random

# define GLOBAL CONSTANTS -- Python "style guides" recommend all upper case with underscores
ROCK = 1
PAPER = 2
SCISSORS = 3


# the main function includes the main game logic

# display welcome message
def main():
    print("welcome! lets plau rock paper scissors")

    computer_choice = get_computer_choice()
    player_choice = get_player_choice()
    display_results(computer_choice, player_choice)
    while computer_choice == player_choice:
        computer_choice = get_player_choice()
        display_results(computer_choice, player_choice)
        print("\nthanks for playing")

    # set initial values for computer_choice and player_choice
    # they need to be equal to one another so the while loop will be executed at least once

    # if there is a tie, keep trying until someone wins

    # get a random choice for the computer

    # get a choice from the player

    # display an appropriate response

    # display exit message


# the get_computer_choice() function returns a random number between 1 and 3
def get_computer_choice():
    return random.randint(1, 3)


# player_choice() needs to get an integer value from the user, validate it, and return a valid choice
def get_player_choice():
    choice = "0"  # "0" is not a valid answer, so the loop will run at least once

    # create a validation loop to ask for and validate the answer
    while choice != "1" and choice != "2" and choice != "3":
        print("\nWhat will you choose:")
        print("   1. rock")
        print("   2. paper")
        print("   3. scissors")
        choice = input("? ")  # strip off spaces just in case

    # once we exit the loop, the choice has been validated
    return int(choice)


# display the results, showing who chose what and who wins (or if there is a tie)
# arguments are the computer's choice and the player's choice as values 1, 2, or 3
def display_results(computer, player):
    print("\nThe computer chose", translate(computer), "and you chose", translate(player))
    if player == computer:
        print("No winner. Try again.")
    elif computer == ROCK:
        if player == PAPER:
            print("Paper covers rock. You win!")
        else:  # player == scissors
            print("Rock breaks scissors. Computer wins.")
    elif computer == PAPER:
        if player == ROCK:
            print("Paper covers rock. Computer wins.")
        else:  # player == scissors
            print("Scissors cut paper. You win!")
    else:  # computer == SCISSORS
        if player == PAPER:
            print("Scissors cut paper. Computer wins.")
        else:  # player == ROCK
            print("Rock breaks scissors. You win!")


# translate the numeric choice into a word
def translate(numeric_choice):
    if numeric_choice == ROCK:  # testing against global constant values
        return "rock"
    elif numeric_choice == PAPER:
        return "paper"
    elif numeric_choice == SCISSORS:
        return "scissors"
    else:
        return "invalid choice"  # if everything is working properly, this should never appear


# main program
main()
