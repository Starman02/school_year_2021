"""Write a program that calculates the amount of money a person would earn over a period of time if his or her salary is one penny the first day, two pennies the second day, and
continues to double each day. The program should ask the user for the number of days. Display a table showing what the salary was for each day, and then show the total pay at
the end of the period. The output should be displayed in a dollar amount, not the number of pennies.
Hint: use Range, set the field size in formatting.
Use the range version of the for statement
Set the field size in formatting money (review chapter 2 on formatting)
"""
desiredDays = int(input("How Many days would you like to work?: "))
pay = 0.00
pennies = .01
print("DAYS WORKED| AMOUNT EARNED THAT WAY")
print("____________________________________________")
for d in range(1, desiredDays+1):
    print(d, "|$\t", format(pennies, ',.2f'))
    pennies *= 2
    pay += pennies

print("Total earned over: ", desiredDays, "days is: ", format(pay, ',.2f'))
