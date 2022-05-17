"""Running on a treadmill you burn 4.2 calories per minute. Write a program that uses a loop to display the number of calories burned after 10, 15, 20, 25 and 30 minutes.

"""
calBurnRate = 4.2       # rate at which calories are burned
Caltotal = 0
for cal in range(10, 31, 5):        # starts at 10, goes to 30 in 5 incraments
    Caltotal = cal * calBurnRate        # does the calorie math
    print("You have burned ", Caltotal, "in", cal)
