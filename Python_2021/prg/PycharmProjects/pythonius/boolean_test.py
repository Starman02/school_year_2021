"""A boolean variabble holds either true or false, true and false must be capitalized"""
it_is_raining = True
if it_is_raining:
    print("slabadabala")

# input gets string, mudt make boolean
x = int(input("Enter the first integer: "))
y = int(input("Enter the second integer: "))

if x < y:
    print(x, "is less than ", y)
elif x > y:
    print(x, "is greater than ", y)
else:
    print(x, "and ", y, "are equal")

# using a chained if to find a letter grade
score = float(input("enter the test score: "))  # a float can have a fractioal part
if score >= 90.0:
    print("You got an A")
elif score >= 80.0:
    print("YOU GOT A B")
elif score >= 70.0:
    print("YOU GOT A C")
elif score >= 60.0:
    print("YOU GOT A D")
else:
    print("you failed")

some_number = int(input("enter a number: "))
if some_number >= 0:
    if some_number == 0:
        print("you entered a 0")
    else:
        print("you entered a positive number")
else:
    print("you entered a negative number")
