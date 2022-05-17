"""
Design a class that holds the following personal data: name, address, age, and phone number. Write appropriate accessor and mutator methods (get
and set). Write a program that creates three instances of the class. One instance should hold your information and the other two should hold your
friends or family members' information.  Just add information, don't get it from the user.  Print the data from each object, make sure to format the
output for clarity and ease of reading.

OUTLINE:
PERSON_DATA
*** THIS IS THE __INIT, it defines the parameters
-name:String
-address:string
-age:int
-phone:string
_________
+ set_name *
+ set_address *
+ set_age *
+ set_phone *
+ get_name *
+ get_address *
+ get_age *
+ get_phone *
+ string function

"""


class Persondata:
    # constructor
    def __init__(self, name, address, age, phone):  # gives constructor parameters
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone

        # Mutators

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone(self,
                  phone):  # *** set_name takes the information from get_name and then makes name whatever it was assigned in the call for the class
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone(self):
        return self.__phone

    def __str__(self):
        data = "Name: " + self.__name
        if self.__address is not None:
            data += "\nAddress: " + self.__address
        if self.__age is not None:
            data += "\nAge: " + self.__age
        if self.__phone is not None:
            data += "\nPhone Number: " + self.__phone
        return data

def main():
    devin = Persondata("Devin", "the caribian sea", "19", "708-227-4381")
    print(devin)
    print("_" * 10)
    joey = Persondata("Joey", "The pacific ocean", "17", "708-788-8764")
    print(joey)
    print("_" * 10)
    don = Persondata("Don", "The atlantic ocean", "44", "815-676-8989")
    print(don)


main()
