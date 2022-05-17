"""
In the first step, you will create a parent class. Create a parent class for Office Furniture. Set the class attributes to be category (desk, chair, filing cabinet would be example values), material, length, width, height, and price. Include a method that returns a string about the
object. Implement the __str__ method (refer to section 10.2 in your book for details).

"""

class Office_furniture:
    # the different values category could become
    CATEGORIES = {1: "Desk", 2: "Chair", 3: "Cabinet", 4: "Table"}
    MATERIAL = {1: "Spruce", 2: "Oak", 3: "Cloth", 4: "Plastic"}

    def __init__(self, category=None, material=None, length=None, width=None, height=None, price=None):
        self.__category = None
        self.set_category(category)  # does data validation
        self.__material = None
        self.set_material(material)  # more validation
        self.__length = length
        self.__width = width
        self.__height = height
        self.__price = price

        # setters

    def set_category(self, category):
        if category in Office_furniture.CATEGORIES:
            self.__category = category

    def set_material(self, material):  # tests to see whether a condition entered actually exists
        if material in Office_furniture.MATERIAL:
            self.__material = material

    def set_length(self, length):
        self.__length = length

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def set_price(self, price):
        self.__price = price

        # mutators

    def get_category(self):
        return self.__category

    def get_material(self):
        return self.__material

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_price(self):
        return self.__price

    def __str__(self):

        return "This Office Item is a " + Office_furniture.CATEGORIES[self.__category] + " which is made of " + \
               Office_furniture.MATERIAL[
                   self.__material] + "\n this item has the following dimensions: " + "\nA length of" + self.__length + "\nA width of " + self.__width + "\n With a height of" + self.__height + "\n for a total cost of: " + self.__price

# needs a new class called categories, which will determine what the object is
