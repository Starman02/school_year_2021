# the Card class has all the attributes and methods needed to create a Card
class Card:
	# these are class attributes
	# class attributes are defined OUTSIDE of the __init__() method
	# all instances of the class share one set of class attributes
	# class attributes are accessed by using the name of the class, like Card.SUITS
	# these attributes are CONSTANTS (the value doesn't change), so the name is all uppercase
	SUITS = {'S': '\u2660', 'H': '\u2661', 'C': '\u2663', 'D': '\u2662'}  # unicode values
	FACE_CARDS = {1: "A", 11: "J", 12: "Q", 13: "K"}

	# this is the constructor method: __init__()
	# it creates the instance attributes -- every instance (object) has its own set of instance attributes
	# instance attributes are preceded by self. to identify which object they belong to
	# using double underscore to begin the name makes the attribute PRIVATE (hidden)
	# using default values for parameters specifies the value to use when/if they are omitted
	def __init__(self, suit=None, rank=None):
		self.__suit = suit
		self.__rank = rank

	# accessors (getters)
	def get_suit(self):
		return self.__suit

	def get_rank(self):
		return self.__rank

	def get_card(self):
		return self.__str__()

	# mutators (setters) -- setters should validate the data before setting (when appropriate)
	def set_suit(self, suit):
		if suit.upper() in Card.SUITS:
			self.__suit = suit.upper()
		else:
			self.__suit = None

	def set_rank(self, rank):
		if rank.isdigit():
			if rank in range(1, 14):
				self.__rank = rank
			else:
				self.__rank = None
		else:
			self.__rank = None

	# return the string representing a face card
	def face_card(self):
		if self.__rank in Card.FACE_CARDS:
			return Card.FACE_CARDS[self.__rank]

	# __str__() returns a string representation of the Card
	# every "path" through the logic must end in a return statement
	def __str__(self):
		if self.__rank is None or self.__suit is None:
			return None
		else:
			if self.__rank in self.FACE_CARDS:
				return Card.FACE_CARDS[self.__rank] + Card.SUITS[self.__suit]
			else:
				return format(self.__rank, "d") + Card.SUITS[self.__suit]
