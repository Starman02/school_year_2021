import random
import math
"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""


# TODO 5.2 - calling an existing function
print("=" * 10, "Section 5.2 call an existing function", "=" * 10)
# Beneath the following function, write the code to call it
# Remove the """ """ before testing
# Note: Python requires two blank lines before a function definition


def hello():
    print("Hello Sweetie!")

# Write the code to call the hello function on the next line
hello()

# TODO 5.2 - creating and calling a function
print("=" * 10, "Section 5.2 create and call an existing function", "=" * 10)
# Write a function called joke that prints a joke on the screen
# Call the function
def joke():
    print("why did the chicken cross the road? to get to work and provide for her family, shes running late and so are you, stop questioning a chicken")

joke()


# TODO 5.3 designing a program in functions
print("=" * 10, "Section 5.3 design a program using functions", "=" * 10)
# Create a main function that will call separate functions that
# print each line in a knock knock joke. Make sure to call main
# as the last line of your code.


def the_greatest_joke():
    print("Knock knock")

def the_greatest_response():
    print("whos there?")

def the_greatest_setup():
    print("bannana")

def the_mostmid_question():
    print("bannana who?")

def the_greatestjokeofthecentry():
    print("It's peanut butter jelly time Peanut butter jelly time Peanut butter jelly time Where he at? Where he at? Where he at? Where he at? Now there he go, there he go There he go, there he go Peanut butter jelly, peanut butter jelly Peanut butter jelly, peanut butter jelly Do the peanut butter jelly, peanut butter jelly Peanut butter jelly with a baseball bat Do the peanut butter jelly, peanut butter jelly Peanut butter jelly with a football cap Now where he at? Where he at? Where he at? Where he at? Now there he go, there he go There he go, there he go Peanut butter jelly, peanut butter jelly Peanut butter jelly, peanut butter jelly Do the peanut butter jelly, peanut butter jelly Peanut butter jelly with a baseball bat Do the peanut butter jelly, peanut butter jelly Peanut butter jelly with a football cap Now break it down and freeze (freeze) Take it down to your knees (knees) Now lean back and freeze (freeze) Now get back up and freeze (freeze) Now where he at? Where he at? Where he at? Where he at? Now there he go, there he go There he go, there he go Peanut butter jelly, peanut butter jelly Peanut butter jelly, peanut butter jelly Do the peanut butter jelly, peanut butter jelly Peanut butter jelly with a baseball bat Do the peanut butter jelly, peanut butter jelly Peanut butter jelly with a football cap Now sissy walk, sissy walk Sissy walk, you go, boy Sissy walk, sissy walk Hell no (I don't wanna hear you say that) Where he at? Where he at? Where he at? Where he at? Now there he go, there he go There he go, there he go Peanut butter jelly, peanut butter jelly Peanut butter jelly, peanut butter jelly Do the peanut butter jelly, peanut butter jelly Peanut butter jelly with a baseball bat Do the peanut butter jelly, peanut butter jelly Peanut butter jelly with a football cap It's the brand new song all across the land Do the peanut butter jelly, how you do that dance? Put your hands to the side, ball your fists up, y'all Watch a little shorty like this, big dawg Ride to the style we throwin' down And lean back all the way to the ground Buckwheat Boyz, we in the house So say it loud, lemme hear you shout Now walk, walk, walk with it Stomp, stomp, stomp with it Slide, slide, slide with it Bring it back one more time Walk, walk, walk with it Stomp, stomp, stomp with it Slide, slide, slide with it Peanut butter jelly, breakdown Throw the ball up, swing that bat Tilt your head back and see where it's at Throw the ball up and swing that bat Tilt your head back, lemme see where it's at Peanut butter jelly, peanut butter jelly Peanut butter jelly, peanut butter jelly Do the peanut butter jelly, peanut butter jelly Peanut butter jelly with a baseball bat Do the peanut butter jelly, peanut butter jelly Peanut butter jelly with a football cap Now freestyle, freestyle your style Freestyle, freestyle my style Freestyle, freestyle their style Freestyle, freestyle, buck wild Where he at? Where he at? Where he at? Where he at? Now there he go, there he go There he go, there he go")

def main():
    the_greatest_joke()
    the_greatest_response()
    the_greatest_setup()
    the_mostmid_question()
    the_greatestjokeofthecentry()

main()

# TODO 5.4 local variables
print("=" * 10, "Section 5.4 using local variables", "=" * 10)
# 1) Write a program with a main2 function. In main2, define a variable
#    called name and assign a name to it, then print hello
#    and the name variable. Have main2 call a second function get_name().
# 2) In the get_name function, ask the user for their name,
#    then greet them using a print statement.
# 3) Call the main2 function.
# Note - you would not normally have more than one main function
# in a program, we are just adding the number after main to allow
# us to write multiple short practice programs in a single file.


def get_name():
    name = input("Whats your name?")
    print("Welcome ", name)


def main2():
    name = "bobby"
    print("welcome ", name)
    get_name()

main2()


# TODO 5.5 passing arguments to Functions
print("=" * 10, "Section 5.5 passing arguments", "=" * 10)
# Complete the code below to pass the my_number variable value from
# main3() into square() using a parameter name of value.
# Remove the """ """ before testing


def main3():
    my_number = 7
    square(my_number)
    
    
def square(value):
    squared_value = value * value
    print(squared_value)
    
    
main3()



# TODO 5.5 passing multiple arguments
print("=" * 10, "Section 5.5 passing multiple arguments", "=" * 10)
# Complete the code below to pass the variables from main into
# parameters for add. Look at the code to determine the correct
# variable / parameter names. Remove the """ """

def main4():
    num_one = 5
    num_two = 7
    add(num_one, num_two)
    
    
def add(one, two):
    total = one + two
    print(total)


main4()



# TODO 5.7 value returning functions
print("=" * 10, "Section 5.7 value returning functions", "=" * 10)
# import random - Add a statement importing the random library at the top of this file
# Add a global constant PI with a value of 3.14 before the main5 function definition

PI = 3.13


def main5():
    r = random.randint(1, 10)  # TODO generate a random integer between 1-10, assign it to the variable r
    r2 = r * r
    area(r2)
    
    
def area(radius_squared):
    my_area = PI * radius_squared  # TODO insert the PI constant multiplied by the parameter here
    print(format(my_area, ",.2f"))
    
    
main5()


# TODO 5.8 value returning functions
print("=" * 10, "Section 5.8 value returning functions", "=" * 10)
# Complete the following program, remove the """  """ before testing
def main6():
    print("This program will calculate your BMI")
    height = float(input("What is your height in inches?  "))
    weight = float(input("What is your weight in pounds"))
    # TODO call the bmi function and assign the result to a variable named answer
    answer = bmi(weight,height)

    # TODO print the variable answer, make sure to format it to 1 decimal place
    print(format(answer, ".1f"))
    # TODO modify the bmi function to accept the height and weight
    # read the code to determine the parameter names


def bmi(weightInches, heightInches):
   #  BMI = (weightInches/ (heightInches x heightInches)) x 703
    patient_bmi =  (weightInches / (heightInches * heightInches)) * 703
    # TODO send the patient_bmi value back to main6
    return patient_bmi

main6()
# TODO 5.9 the math module
print("=" * 10, "Section 5.9 use the math module", "=" * 10)
# import math - Add the import math statement at the top of this file
# Write a statement that uses the ceil function on the following variable
# Display the result

number_to_round = 4.243
print(math.ceil(number_to_round))
"""
def cookie_fun():
    cookie = "cookies" 
    brownie(cookie)


def brownie_fun(desert): send the value of cookie to brownie                notes for me to look back on

    if desert == "cookies":
        print("this is not a brownie")
    else:
        print("this is a brownie")

cookie()
"""

