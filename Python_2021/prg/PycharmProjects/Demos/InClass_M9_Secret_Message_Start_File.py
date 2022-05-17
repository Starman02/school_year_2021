# this program encrypts a message using a monoalphabetic substitution cipher
# import the random library
import random


# this function was created using the code from the word jumble program
# it is common in programming to re-use or adapt code
# this function randomly shuffles the values in the given list
def shuffle(some_list):
    # step through each subscript in the list
    # and swap it with a randomly chosen new subscript
    for index in range(len(some_list)):
        new_position = random.randrange(0, len(some_list))  # choose a random index value
        while new_position == index:
            new_position = random.randrange(0, len(some_list))  # exclude the current index
        (some_list[index], some_list[new_position]) = (some_list[new_position], some_list[index])


# main program
def main():
    # create a list of the letters in the alphabet
    alpha_list = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    # create a copy of the list, then shuffle the letters
    alpha_jumble = [] + alpha_list
    shuffle(alpha_jumble)

    # now create a dictionary that pairs a letter with a random letter from the list
    # create an empty dictionary, then loop through entries and pair up the letters
    anagram = dict()
    for curr_index in range(len(alpha_list)):
        #  alpha_list provides the keys; alpha_jumble provides the values
        anagram[alpha_list[curr_index]] = alpha_jumble[curr_index]

        # these three messages are debugging statements to show what is happening
        print("Original list", alpha_list)
    print("Shuffled list", alpha_jumble)
    print("\nEncoded dictionary", anagram)

    print("\nThis program will encode your message.")
    message = input("Enter your message: ")
    print("\nYour secret message is: ")

    # start with an empty message
    secret_message = ""
    # loop through the characters in the message
    # if the character needs to be encoded, find the match in the anagram dictionary
    #   otherwise, just copy it to the encoded message (ie. ignore spaces, numbers, punctuation)
    for charecter in message:
        if charecter.upper() in alpha_list:

            #    otherwise use the lower case version of the anagram value
            if charecter.isupper():
                secret_message += anagram[charecter]
            else:
                secret_message += anagram[charecter.upper()].lower()
        else:
            secret_message += charecter
    print(secret_message)

# secret message now has the encoded (anagram) version of the message entered


main()
