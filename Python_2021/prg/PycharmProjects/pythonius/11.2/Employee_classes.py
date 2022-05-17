"""
Write an Employee class that keeps data attributes for the following pieces of information:

Employee name
Employee number

Next, Write a class named ProductionWorker that is a subclass of the Employee class. The ProductionWorker class should keep data attributes for the following information

Shift numbered (an integer, such as 1, 2, or 3)
Hourly pay rate

The workday is divided into two shifts: day and night. The shift attribute will hold an integer value representing the shift that the employee works. The day shift is shift 1 and the night shift is shift 2.


"""


class Employee:

    # main constructor
    def __init__(self, employee_name, employee_number):
        self.__employee_name = employee_name
        self.__employee_number = employee_number

    # setters
    def set_employee_name(self, employee_name):
        self.__employee_name = employee_name

    def set_employee_number(self, employee_number):
        self.__employee_number = employee_number

    # getters

    def get_employee_name(self):
        return self.__employee_name

    def get_employee_number(self):
        return self.__employee_number

    def __str__(self):
        return "\nDetails of employee" + "\nName: " + self.__employee_name + "\nEmployee Number: " + self.__employee_number


class Production_Worker(Employee):
    # main Attributes
    SHIFTS = {1: "Day", 2: "Night"}

    #  sub constructor
    def __init__(self, employee_name, employee_number, shift, hourly_rate):
        super().__init__(employee_name, employee_number)
        self.__shift = shift
        self.__hourly_rate = hourly_rate

    # setters

    def set_shift(self, shift):
        if shift in Production_Worker.SHIFTS:
            self.__shift = shift
        else:
            self.__shift = "Invalid Shift Type"

    def set_hourly_rate(self, hourly_rate):
        self.__hourly_rate = hourly_rate

    # getters
    def get_shif(self):
        return self.__shift

    def get_hourly_rate(self):
        return self.__hourly_rate

    def __str__(self):
        final_assembly = Employee.__str__(self)
        return final_assembly + "\nShift Type: " + Production_Worker.SHIFTS[
            self.__shift] + "\nPay Rate: " + "$" + self.__hourly_rate
