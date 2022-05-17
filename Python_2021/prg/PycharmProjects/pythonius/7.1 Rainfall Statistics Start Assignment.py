"""
Copy program 4.3 into the chapter 7 folder and rename it as "7-1-Rainfall-Statistics"
Modify the program so that the rainfall for each month is stored into a list. Eliminate the user's ability to select the number of
years, you will just work with one year's data.   The program should calculate and display the total rainfall for the year, the
average monthly rainfall the year, and the months with the highest and lowest amounts of rain for the year. Hint: convert
months to a list so you can use the index value to print the max and min months.

"""


def rainfall():
    totalrain = 0.0
    monthcount = 0.0
    years = 1
    monthsofyear = []
    months = ["Janurary", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    for r in range(years):  # outer loop, for calculating years
        print("Year ", r + 1)
        for month in range(len(months)):  # inner loop aks for rain of every month
            try:

                print("How many inches of rainfall for", months[month], ":")
                rainfall = float(input())
                monthsofyear.append(rainfall)
                totalrain += rainfall  # adds all rainfall together for each month
                monthcount += 1  # counts every month for division
            except ValueError:
                print("Error, value must be a integer or decimal, skipping month")

    minimum = min(monthsofyear)
    maximum = max(monthsofyear)

    min_months = monthsofyear.index(minimum)
    max_months = monthsofyear.index(maximum)

    print("Total amount of recorded Rainfall: ", format(totalrain, ".2f"))
    averageRainfall = totalrain / monthcount
    print("Average rainfall: ", format(averageRainfall, '.2f'))

    print("The Minimum Amount of rainfall is: ", minimum, 'which occured during', months[min_months])
    print("The Maximum Amount of rainfall is: ", maximum, "which ocured during", months[max_months])


rainfall()
