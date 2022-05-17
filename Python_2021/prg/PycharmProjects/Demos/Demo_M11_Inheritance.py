class Transport:
	# class attributes (constants)
	MODES = {1: 'land', 2: 'sea', 3: 'air'}
	CARGO_TYPE = {1: 'freight', 2: 'people'}

	# constructor
	def __init__(self, mode=None, cargo=None):
		self.__mode = None
		self.set_mode(mode)  # do the data validation
		self.__cargo = None
		self.set_cargo(cargo)

	# setters -- validate and set value
	def set_mode(self, mode):
		if mode in Transport.MODES:
			self.__mode = mode

	def set_cargo(self, cargo):
		if cargo in Transport.CARGO_TYPE:
			self.__cargo = cargo

	# getters
	def get_mode(self):
		return self.__mode

	def get_cargo(self):
		return self.__cargo

	# string representation
	def __str__(self):
		return "This is a " + Transport.MODES[self.__mode] + " vehicle that transports " + Transport.CARGO_TYPE[
			self.__cargo] + "."


# the class Car is a child of the class Transport -- it inherits the attributes and methods of its parent
class Car(Transport):
	# constructor
	def __init__(self, make=None, model=None, year=None, color=None):
		Transport.__init__(self, 1, 2)		# 1=land, 2=people
		self.__make = make
		self.__model = model
		self.__year = year
		self.__color = color

	# setters -- some data validation should occur here
	def set_make(self, make):
		self.__make = make

	def set_model(self, model):
		self.__model = model

	def set_year(self, year):
		if isinstance(year, int):
			if year > 1750:
				self.__year = year

	def set_color(self, color):
		self.__color = color

	# string representation
	def __str__(self):
		result = Transport.__str__(self)
		if self.__make is None and self.__model is None and self.__year is None and self.__color is None:
			return result + "Details for this vehicle are unknown."
		else:
			result += " It is a"
			# add details one by one
			if self.__color is not None:
				result += " " + self.__color
			if self.__year is not None:
				result += " " + str(self.__year)
			if self.__make is not None:
				result += " " + self.__make
			if self.__model is not None:
				result += " " + self.__model
			return result + "."


def main():
	generic = Transport(2, 2)
	print(generic)
	generic.set_cargo(1)
	print(generic)

	my_car = Car('Ford', 'Mustang', 1980, 'blue')
	print(my_car)
	van = Car('Chrysler', 'Town and Country', 1992, 'forest green')
	print(van)
	print(my_car)

	van.set_color('electric blue')
	print(van)

	unknown = Car()
	print(unknown)

	partially_unknown = Car("BMW")
	print(partially_unknown)

	# can leave out parameters, but cannot just put commas -- need to use None
	another_one = Car(None, "mustang")
	print(another_one)


main()
