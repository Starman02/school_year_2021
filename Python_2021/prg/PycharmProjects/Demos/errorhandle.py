a = 17
b = 0

# the following code will generate an error
# print(a / b)


#   wrong way
try:
    print(a / b)
#
except:  # unspecofoed exception generates a warning, not proper, need to use axception or use an error  code
    print("an error occurred!")


#   right way
try:
    print(a / b)
except ZeroDivisionError:
    print("you cannot divide by zero")


c = '0'
#   print(a / c)
try:
    print(a / c)
except TypeError:
    print("Your data is the wrong type")

invalue = input("\nplease enter a number")

try:
    float_value = float(invalue)
    print(format(float_value, ".2f"))
except ValueError:
    print("expected a floating point value.")

#   there are some specific error file handling exceptions, or you can use the IOerror to catch any file access error
try:
    infile = open('doesnotexists.txt')
except IOError:
    print("Could not open file")
