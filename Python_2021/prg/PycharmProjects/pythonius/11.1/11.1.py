from Office_class import Office_furniture
from Desk_class import Desk

"""
In the first step, you will create a parent class. Create a parent class for Office Furniture. Set the class attributes to be category (desk, chair, filing cabinet would be example values), material, length, width, height, and price. Include a method that returns a string about the
object. Implement the __str__ method (refer to section 10.2 in your book for details).

In the second step create a subclass for Desk that includes location_of_drawers (left, right both are options) and number_drawers. Override the parents __str__ method to include drawer location and count. In the Desk class, the __init__() method should set the parent
attribute category to "Desk".

Implement each class in a separate file. Import these into your main program. Your main program should implement and display an instance of each, the parent class and the child class.
"""


def main():
    plastic_desk = Office_furniture(1, 4, " 8.9 feet", " 5.5 feet", " 8 feet", "$1000")
    print(plastic_desk)
    print("________" * 10)
    spruce_desk = Office_furniture(1, 1, " 9.9 feet", " 6.5 feet", " 9 feet", "$900")
    print(spruce_desk)
    print("________" * 10)
    oak_chair = Office_furniture(2, 2, " 2 feet", " 4 feet", " 4 feet", "$600")
    print(oak_chair)
    print("________" * 10)
    cloth_cabinet = Office_furniture(3, 3, " 6 feet", " 5 feet", " 9 feet", "$540")
    print(cloth_cabinet)
    print("________" * 10)
    oak_table = Office_furniture(4, 2, " 8 feet", " 8 feet", " 5.6 feet", "$430")
    print(oak_table)
    print("________" * 10)
    deskquestions = Desk(2, "3")
    print(plastic_desk , deskquestions)

main()
