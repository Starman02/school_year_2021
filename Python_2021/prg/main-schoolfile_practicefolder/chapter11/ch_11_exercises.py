"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""

# TODO 11.1 Introduction to Inheritance
print("=" * 10, "Section 11.1 inheritance", "=" * 10)


# You are going to create a Dwelling class based on the
# Automobile sample from the chapter

# 1) Create the class Dwelling, the __init__ method should accept number_of_rooms, square_feet, floors
class Dwelling:
    def __init__(self, number_of_rooms, square_feet, floors):
        self.__number_of_rooms = number_of_rooms
        self.__square_feet = square_feet
        self.__floors = floors

    # 2) Add mutators for all of the data attributes (number_of_rooms, square_feet, floors)
    def set_number_of_rooms(self, number_of_rooms):
        self.__number_of_rooms = number_of_rooms

    def set_square_feet(self, square_feet):
        self.__square_feet = square_feet

    def set_floors(self, floors):
        self.__floors = floors

    # 3) Add accessors for all of the data attributes

    def get_number_of_floors(self):
        return self.__number_of_rooms

    def get_square_feet(self):
        return self.__square_feet

    def get_floors(self):
        return self.__floors

    def __str__(self):
        return "This house has " + self.__number_of_rooms + " This house also has " + self.__square_feet + " This house has: " + self.__floors


# 4) Create the class SingleFamilyHome as a sub class of Dwelling
# The __init__ method should accept number_of_rooms, square_feet, floors, garage_type, yard_size
# -- Call the __init__ of superclass Dwelling and pass the required arguments, remember to include self
# -- Initialize the garage_type and yard_size attributes
class SingleFamilyHome(Dwelling):
    # 5) Create the mutator and accessor methods for the garage_type and yard_size attributes
    def __init__(self, number_of_rooms, square_feet, floors, garage_type, yard_size):
        Dwelling.__init__(self, number_of_rooms, square_feet, floors)
        self.__garage_type = garage_type
        self.__yard_size = yard_size

    def set_garage_type(self, garage_type):
        self.__garage_type = garage_type

    def set_yard_size(self, yard_size):
        self.__yard_size = yard_size

    def get_garage_type(self):
        return self.__garage_type

    def get_yard_size(self):
        return self.__yard_size

    # def __str__(self):
    # 		return "This is a " + Transport.MODES[self.__mode] + " vehicle that transports " + Transport.CARGO_TYPE[
    # 			self.__cargo] + "."
    def __str__(self):
        homestats = Dwelling.__str__(self)
        homestats += " garage type is: " + self.__garage_type + " With a yard size of " + self.__yard_size
        return homestats


# Demonstrate the SingleFamilyHome class, no need to import because you are in the same file
# 6) Create a main function.
def main():
    # 7) In main, create an object from the Single_family_home class with the following information:
    #            6 rooms, 1200 square feet, 1 floor, single car garage, .25 acres
    home1 = SingleFamilyHome("6 Rooms", "1200 Square Feet", "1 floor", "single Car garage", ".25 Acres")
    # 8) Display the data using the accessor methods
    print(home1)


# 9) Call the main function
main()

# TODO 11.2 Polymorphism
print("=" * 10, "Section 11.2 polymorphism", "=" * 10)


# 1) Type in the mammal class from program 11-9, lines 1 - 22
class Mamal:
    def __init__(self, species):
        self.__species = species

    def show_species(self):
        print('I am a species', self.__species)

    def make_sounds(self):
        print("grrrr")


# 2) Create a Mouse class as a sub class of the mammal class following the Dog example
class Mouse(Mamal):
    def __init__(self):
        Mamal.__init__(self, "Mouse")

    def make_sounds(self):
        print("SQWEAK")


# 3) Create an Sheep class as a sub class of the mammal class following the Cat Example
class Sheep(Mamal):
    def __init__(self):
        Mamal.__init__(self, "Sheep")

    def make_sound(self):
        print("BAAAAAH")


# 4) Follow the example in program 11-10 (no need to import, use main2 instead of main
#    because there is already a main on this page) use the Mouse and Sheep class that you created


def main2():
    mammal = Mamal('regular mamal')
    mouse = Mouse()
    sheep = Sheep()

    print("Here are some animals and how they sound!")
    Sheep.show_species(sheep)
    Mouse.show_species(mouse)
    Sheep.make_sound(sheep)
    Mouse.make_sounds(mouse)



main2()
