# range function returns a sequence of values
# when one arguement is specified, it repeats an ending limit (not a ending value)
# endng limit meabs up to not including
# when  a begining value is not specified, it starts at 0
print("Results of range(3)")
for num in range(3):
    print(num)

# when two arguments are specified, they represent a starting value and ending limit
print("\n Results of range(6,10")
for num in range(6, 10):
    print(num)

# when three arguments are specified, the last one is a step value-- default is +1
print("\n the range of (2,11,2")
for num in range(2, 11, 2):
    print(num)

    print("\n the results of range(100,0,-10)")
for num in range(100, 0, -10):
    print(num)

# arguments can be literals or variables
start = 75
end = 100
step = 5
for num in range(start, end, step):
    print(num)

# if you want to include the end value
print("\nResult of range(start,end+1,step")
for num in range(start, end+1, step):
    print(num)

# what range() is doing for you
# if i use range(start,end+1,step), this would give us the same result
for num in [75, 80, 85, 90, 100]:
    print(num)

# you must use a while loop if the number of interactions is not clear
num = 2
end = 250
print("\nThe Squares less than", end, "Are: ")
while num * num < end:
    print(num, "squared is", num * num)
    num += 1        # unlike for loop, I have to make sure num gets an updated value
