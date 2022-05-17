# A class definition is tailored to the application.
# For example, the following Dog class might be used by a Dog Grooming application.
# Class Diagram for the Dog class:
#
#  ###########################################
#  #             Dog                         #   > the name of the class
#  ###########################################
#  # -name: String                           #   \
#  # -breed: String                          #    \
#  # -owner: String                          #     > the attributes (variables)
#  # -preferred_cut: String                  #    /  the - indicates a private attribute
#  # -behavior: String                       #   /
#  ###########################################
#  # + set_name(name: String)                #   \
#  # + set_breed(breed: String)              #    \
#  # + set_owner(owner: String)              #     \
#  # + set_preferred_cut(preferred: String)  #      \
#  # + set_behavior(behavior: String)        #       \
#  # + get_name()                            #        > the methods (functions)
#  # + get_breed()                           #       /  the + indicates public methods
#  # + get_owner()                           #      /
#  # + get_preferred_cut()                   #     /
#  # + get_behavior()                        #    /
#  # - __str__()                             #   /
#  ###########################################


# to define a class in Python, use the keyword class followed by a capitalized class name
class Dog:
    # the constructor method is called when a new object is instantiated
    # def __init__(self, name, breed, owner, preferred, behavior):
    # default values can be included in the parameter list using =
    # when default values are specified, arguments can be left out of the instantiation
    def __init__(self, name="Dog", breed="mutt", owner=None, preferred=None, behavior=None):
        self.__name = name
        self.__breed = breed
        self.__owner = owner
        self.__preferred_cut = preferred
        self.__behavior = behavior

    # mutators (setters)
    # if data validation is needed, it should occur in the mutator method
    def set_name(self, name):
        self.__name = name

    def set_breed(self, breed):
        self.__breed = breed

    def set_owner(self, owner):
        self.__owner = owner

    def set_preferred_cut(self, preferred):
        self.__preferred_cut = preferred

    def set_behavior(self, behavior):
        self.__behavior = behavior

    # accessors (getters)
    # getters usually just return the value,
    # but a simple internal key could be stored and a dictionary used to return a value
    def get_name(self):
        return self.__name

    def get_breed(self):
        return self.__breed

    def get_owner(self):
        return self.__owner

    def get_preferred_cut(self):
        return self.__preferred_cut

    def get_behavior(self):
        return self.__behavior

    # the string method returns a printable summary of the object as a string
    # for example, if you print() the object, this method will supply the string
    # remember, you will need to convert numeric attribute values, if any, to a string
    def __str__(self):
        summary = self.__name + " is a " + self.__breed
        if self.__owner is not None:
            summary += " owned by " + self.__owner
        summary += ". "
        if self.__preferred_cut is not None:
            summary += "The preferred cut for this dog is " + self.__preferred_cut + ". "
        if self.__behavior is not None:
            summary += "Behavior is " + self.__behavior + ". "
        else:
            summary += "Behavior is unknown. "
        return summary


def main():
    # instantiate an object of class Dog
    my_dog = Dog("Logan", "Scottish Terrier", "Cindy", "traditional short", "friendly")
    print(my_dog)
    # instantiate an object of class Dog using default values (if any)
    my_dog2 = Dog()
    print("\n", my_dog2, sep="")
    # modify the cut using a setter, and use getters to grab details
    my_dog.set_preferred_cut("traditional long")
    print("\n", my_dog, sep="")
    print(my_dog2)
    print(my_dog.get_name())
    print(my_dog.get_owner(), "has a", my_dog.get_breed())
    # adding class objects to a list and iterating through the list
    list_of_dogs = [my_dog, my_dog2, Dog("Fido", "German Shepherd", "John", None, "friendly")]
    print(list_of_dogs)
    for puppy in list_of_dogs:
        print(puppy)


main()
