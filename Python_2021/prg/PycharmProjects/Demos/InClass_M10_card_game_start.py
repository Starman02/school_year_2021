from M10_card import Card
from M10_deck import Deck


# import m10_card requires more work to import parts from file, would be easier to import a specific class Id want to use
# can also use from M10_card import * to import all parts from a file


# main program logic
def main():
    # instantiate one single card -- an Ace of hearts
    ace_of_hearts = Card("H", 1)
    print(ace_of_hearts)

    # instantiate a new deck of cards (it will be a list of Card objects)
    deck = Deck()
    # show the full deck for debugging purposes
    for current_card in deck.get_cards():
        print(current_card, end=" ")
    print("")

    # shuffle the deck of cards
    deck.shuffle()

    print("\nLet's play a game.")
    player_hand = []  # this list will hold the player's hand
    computer_hand = []  # this list will hold the computer's hand

    # deal each player 5 cards into their "hand"
    # removes a card from the deck and add it to the hand
    for counter in range(5):
        player_hand.append(deck.deal())
        computer_hand.append(deck.deal())

    # show hands just for debugging purposes
    print("\nYour hand: ", end="")
    for current_card in player_hand:
        print(current_card, end=" ")
    print("\nComputer's hand: ", end="")
    for current_card in computer_hand:
        print(current_card, end=" ")


main()  # start the program
