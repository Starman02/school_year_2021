from M10_card import Card
from M11_deck import Deck


# the cardinal class adds a cardinal value to the suit and rank of a Card
# a cardinal value can be assigned to a card that takes into account
# things like Aces-high, suit-order, or a trump suit
class Cardinal(Card):
	# the init for a Card includes suit and rank as attributes:
	#       def __init__(self, suit=None, rank=None):
	# the Cardinal sub-class also has cardinal as an attribute
	def __init__(self, suit=None, rank=None, cardinal=None):
		Card.__init__(self, suit, rank)
		self.__cardinal = None
		self.set_cardinal(cardinal)



	# the cardinal attribute needs to have a positive integer value
	def set_cardinal(self, cardinal):
		if isinstance(cardinal, int):
			if 1 <= cardinal:
				self.__cardinal = cardinal


	def get_cardinal(self):
		return self.__cardinal

	def card(self):
		return Card.__str__(self)

	# the default display string includes the Card string and cardinal value
	def __str__(self):
		return Card.__str__(self) + "(" + format(self.__cardinal, "d") + ")"



# the Pinochle class creates a pinochle deck
class Pinochle(Deck):
	# the constructor creates a deck of pinochle cards
	def __init__(self):
		Deck.__init__(self)
		self.__trump = None

	# this method sets the trump suit and adjusts cardinal values so that trump outranks all other suits
	def set_trump(self, trump):
		if trump in Card.SUITS:
			self.__trump = trump
			trump_deck = self.get_cards()
			for card in trump_deck:
				if card.get_suit() == self.trump:
					card.set_


	# a pinochle deck has two of each of the cards 9 through A in each suit
	def _make_deck(self):
		new_deck = []
		for suit in Card.SUITS:
			# for debugging purposes, cards are instantiated in Pinochle order
			for rank in [9, 11, 12, 13, 10, 1]:
				new_deck.append(Cardinal(suit, rank, self.__pinochle_cardinal(rank)))
				new_deck.append(Cardinal(suit, rank, self.__pinochle_cardinal(rank)))
		self.set_deck(new_deck)

	# return the correct cardinal value for the given rank of a pinochle card
	# card order for Pinochle is: 9, J, Q, K, 10, A
	@staticmethod
	def __pinochle_cardinal(rank):
		# set Ace to be highest
		if rank == 1:
			return 15
		# set 10 to be second highest
		elif rank == 10:
			return 14
		# nothing else changes
		else:
			return rank


def main():
	# make a deck of pinochle cards
	deck_of_cards = Pinochle()

	print("Display the top card in the deck, with or without the cardinal value")
	# we can display the top card in the deck with the cardinal value
	print(deck_of_cards.get_cards()[0])
	# or just the card alone, using the .card() method provided by the Cardinal class
	print(deck_of_cards.get_cards()[0].card())

	print("\nDisplay the full deck of cards in un-shuffled order with cardinal value")
	print("There should be two each of 9, J, Q, K, 10, A")
	# to display the deck of cards, get the stack of cards and loop through them
	for one_card in deck_of_cards.get_cards():
		print(one_card, end=", ")

	# in Pinochle, players decide on one suit to become trump (Diamonds)
	# try setting the trump suit and show the cards again
	deck_of_cards.set_trump("D")
	print("\n\nNow, trump has been set to", Card.SUITS["D"])
	for one_card in deck_of_cards.get_cards():
		print(one_card, end=", ")


main()
