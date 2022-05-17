"""Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years. The program should first ask for the number of years. The outer loop will iterate once for each year. The inner loop will iterate 12 times, once for each month. Each iteration of the inner loop will ask the user for the inches of rainfall for that month. After all iterations, the program should display the number of months, the total inches of rainfall, and the average rainfall per month for the entire period.

"""
totalrain = 0.0
monthcount = 0.0
years = int(input("how many years would you like to collect data for? (Enter a numerical value): "))
for r in range(years):  # outer loop, for calculating years
    print("Year ", r + 1)
    for months in ("Janurary", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"):  # inner loop aks for rain of every month
        print("How many inches of rainfall for", months, ":")
        rainfall = float(input())
        totalrain += rainfall  # adds all rainfall together for each month
        monthcount += 1  # counts every month for division

print("Total amount of recorded Rainfall: ", format(totalrain, ".2f"))
averageRainfall = totalrain / monthcount
print("Average rainfall: ", format(averageRainfall, '.2f'))
