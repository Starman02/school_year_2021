import random
from M10_card import Card


# the Deck class creates a standard deck and provides methods for simple manipulation
class Deck:
	# the constructor creates a deck of 52 cards
	def __init__(self):
		# create an empty stack to hold the deck of cards
		self.__stack = []
		self._make_deck()

	# this method empties the stack and adds 52 standard cards to the deck
	def _make_deck(self):
		self.__stack = []
		for suit in Card.SUITS:					# knows everything about card class, *can decode face cards* if if cant, my bad ignore this
			for rank in range(1, 14):
				self.__stack.append(Card(suit, rank))



	# this method randomly shuffles the values in the current deck
	def shuffle(self):
		# step through each subscript in the list
		# and swap it with a randomly chosen new subscript
		for index in range(len(self.__stack)):
			new_position = random.randrange(0, len(self.__stack))  # choose a random index value
			while new_position == index:
				new_position = random.randrange(0, len(self.__stack))  # exclude the current index
			(self.__stack[index], self.__stack[new_position]) = (self.__stack[new_position], self.__stack[index])

	# return the number of cards in the deck
	def __len__(self):
		return len(self.__stack)

	# deal a card from the top of the deck (removes the card from the deck)
	def deal(self):
		return self.__stack.pop(0)


	# getters
	def get_cards(self):
		return self.__stack
