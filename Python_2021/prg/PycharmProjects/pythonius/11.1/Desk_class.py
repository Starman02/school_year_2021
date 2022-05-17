from Office_class import Office_furniture

"""
In the second step create a subclass for Desk that includes location_of_drawers (left, right both are options) and number_drawers. Override the parents __str__ method to include drawer location and count. In the Desk class, the __init__() method should set the parent attribute category to "Desk".
"""


class Desk(Office_furniture):
    # Attributes
    DRAWER_LOCATION = {1:"left", 2:"right", 3:"both"}

    def __init__(self, location_of_drawers=None, number_drawers=None, ):
        Office_furniture.__init__(self, 1, None)
        self.__location_of_drawers = None
        self.set_location_of_drawers(location_of_drawers)
        self.__number_drawers = number_drawers

    def set_location_of_drawers(self, location_of_drawers):
        if location_of_drawers in Desk.DRAWER_LOCATION:
            self.__location_of_drawers = location_of_drawers

    def set_number_drawer(self, number_drawers):
        self.__number_drawers = number_drawers

    def get_location_of_drawers(self):
        return self.__location_of_drawers

    def get_number_drawers(self):
        return self.__number_drawers

    def __str__(self):
        return "This desk has " + self.__number_drawers + " the drawers are located on " + Desk.DRAWER_LOCATION[
            self.__location_of_drawers]




# subclass passing, define desk, and location of drawers, once location of drawer is starting, it goes to another class called drawer location, which will get and determine the position of the drawers,
