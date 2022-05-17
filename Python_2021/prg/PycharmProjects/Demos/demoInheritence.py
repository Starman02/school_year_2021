class Transport:
    #class attributes
    MODES = {1: 'land', 2:'sea', 3:'air'}
    CARGO_TYPE = {1:'freight', 2:'people'}

    #constructor
    def __init__(self, mode=None, cargo=None):
        self.__mode = None
        self.set_mode(mode) # do data validation
        self.__cargo = None
        self.set_cargo(cargo)

        #setters
    def set_mode(self, mode):
        if mode in Transport.MODES:
            self.__mode = mode


    def set_cargo(self, cargo):
        if cargo in Transport.CARGO_TYPE:
            self.__cargo = cargo


    def get_mode



        # the class car is a child of trasport, inherits the attributes and methods of parent
class Car(Transport):
    def __init__(self, make=None, model=None, year=None, color=None):
        Transport.__init__(self, 1, 2)              # 1 is land, 2=people
        self.__make = make
        self.__model = model
        self.__year = year
        self.__color = color



    def set_make(self, make):
        self.__make = make


    def set_model(self,model):
        self.__model = model


    def set_year(self, year):
        if isinstance(year, int):
            if year >1750:
                self.__year = year


    def __str__(self):
        result = Transport.__str__(self)
        if self.__make is None and self.__model is None and self.__year is None and self.__color is None:
            return result + "details for this vehicle are unknown"
        else:
            result += " is a "
            # add details one by one
            if self.__color is not None:
                result += " " +str(self.__color)
            if self.__year is not None:
                result += " " +str(self.__year)
            if self.__make is not None:
                result += " " + str(self.__make)
            if self.__model is not None:
                result += " " + str(self.__model)
            return result + "."
