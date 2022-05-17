"""A cookie recipe calls for the following ingredients:

1.5 cups of sugar
1 cup of butter
2.75 cups of flour
The recipe produces 48 cookies with this amount of ingredients. Write a program that asks the user how many cookies they want to make, and then displays the number of cups (to two decimal places) of each ingredient needed for the specified number of cookies.
"""

#constant values for recipie
sugar = 1.5
budder = 1
flour = 75
totalCookies = 48
dream = int(input('ENTER THE DESIRED AMOUT OF COOKIES: '))

dreamSugar = (dream/totalCookies) * sugar
dreambudder = (dream/totalCookies) * budder
dreamflour = (dream/totalCookies) * flour
print("TO MAKE ", dream,"YOU WILL NEED: ")
print(dreamSugar, "Cups of Sugar")

