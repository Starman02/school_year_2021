from Employee_classes import Production_worker

"""
Write an Employee class that keeps data attributes for the following pieces of information:

Employee name
Employee number

Next, Write a class named ProductionWorker that is a subclass of the Employee class. The ProductionWorker class should keep data attributes for the following information

Shift numbered (an integer, such as 1, 2, or 3)
Hourly pay rate

The workday is divided into two shifts: day and night. The shift attribute will hold an integer value representing the shift that the employee works. The day shift is shift 1 and the night shift is shift 2.

File2
Once you have written the classes, write a program that creates an object of the ProductionWorker class and prompts the user to enter data for each of the object’s data attributes. Store the data in the object and then use the object’s accessor methods to retrieve it and display it on the screen.
 
"""


def main():
    data = Production_worker(str(input("Input Your name: ")), str(input("\nEnter your Worker number")),
                             int(input("Enter your Shift number(one for day two for night)")),
                             str(input("input your Hourly Rate")))
    print(data)


main()
