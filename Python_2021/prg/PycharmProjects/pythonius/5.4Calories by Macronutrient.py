"""
A nutritionist who works for a fitness club helps members by evaluating their diets. As part of her evaluation, she asks members for the number of fat
grams, carbohydrate grams, and protein grams that they consumed in a day. Then, she calculates the number of calories that result from the fat, using
the following formula
calories from fat = fat grams X 9

Next, she calculates the number of calories that result from the carbohydrates, using the following formula:
calories from carbs = carb grams X 4

Next, she calculates the number of calories that result from the proteins, using the following formula:

calories from protein = protein grams X 4

Use a different function for each nutrient to make calculations by nutrient, and print the calories for that nutrient on screen.
Return the results from each function to variables in the main method.
Add the variables in the main method to display the total calories for the day.
"""


def main():  # main function to call other functions
    fat = float(input("How many grams of fat have you eaten today?: "))
    carb = float(input("How many Carbohydrate Grams have you eaten today?: "))
    protein = float(input("How many grams of protein have you eaten today?: "))
    print("you ate ", caloriesFatCalculator(fat), "worth of fat calories")  # retrives and prints out various calories ate
    print("you ate ", caloriesCarbCalculator(carb), "worth of carb calories")
    print("you ate ", caloriesproteinCalculator(protein), "worth of protein calories")
    total = caloriesproteinCalculator(protein) + caloriesFatCalculator(fat) + caloriesCarbCalculator(carb)
    print("You ate a total of ", total, "calories today")


def caloriesFatCalculator(tot):  # calculates calories
    print(tot)
    calFromFat = tot * 9
    return calFromFat  # returns calculated fat


def caloriesCarbCalculator(bleem):  # calculates carbs and returns the value. (variable names are very different and random on purpose, will use for refrence)
    calfromcarb = bleem * 4
    return calfromcarb


def caloriesproteinCalculator(example):  # calculates protein, same reasoning for variable name as before
    calFromProtein = example * 4
    return calFromProtein


#   global variables to increase simplicity
main()


