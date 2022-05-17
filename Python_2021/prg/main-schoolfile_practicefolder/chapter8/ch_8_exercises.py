"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""

# TODO 8.1 Basic string Operation
print("=" * 10, "Section 8.1 string operations", "=" * 10)
# 1) Print all the characters from the name variable by accessing one character at a time
name = "John Jacob Jingleheimer Schmidt"
for letter in name:
    print(letter, end=" ")
# 2) Use the index value to access and print the capital s in Schmidt from the variable name

print('\n', name[24])
# 3) Use a negative index value to print the letters from the last name "Schmidt" in name
print(name[-7:])

# TODO 8.2 String slicing
print("=" * 10, "Section 8.2 string slicing", "=" * 10)
# 1) Use string slicing to assign the middle name "Jacob" from name to the variable middle, replace the ""
name.split(" ")

print(name.find('jacob'))

# 2) Print middle
middle = name[5:10]
print(middle)

# TODO 8.3 Testing, Searching, and manipulating strings
print("=" * 10, "Section 8.3 manipulating strings", "=" * 10)
# 1) Test to see if the string "Jacob" is in name, print the result
print(name.find('Jacob'))
if name.find('Jacob') != -1:
    print('jacob has been found')
else:
    print("jacob has been lost")
# 2) Test to see if the string "Michael" is in name, print the result
print(name.find('Michael'))
# 3) Test to see if name contains a number, print the result
print(name.isdigit())
contain_digit = False
for LOR in name:
    if LOR.isdigit():
        contain_digit = True
print(contain_digit)

# 4) Test to see if number contains a number, print the result
number = "42"
if number.isdigit():
    print("Number Contains the number", number)
else:
    print("Number not found")
# 5) Search for "J" in name, replace with "j" (lower case), print the result
#    Note: You can assign this to a variable first, or just print
print(name.replace('J', 'j'))

# 6) Split the string name into the variable name_list, replace the "", print the result
name_list = name.split(' ')
print(name_list)
