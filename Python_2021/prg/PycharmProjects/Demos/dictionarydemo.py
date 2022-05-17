import pickle
# define a dictionary
weekday = {1: 'sunday', 2: 'monday', 3: 'tuesday', 4: 'wedensday', 5: 'thursday', 6: 'friday', 7: 'saturday'}
months = {1: 'january', 2: 'feburary', 3: 'march', 4: 'april', 5: 'may', 6: 'june', 7: 'july', 8: 'august',
          9: "september", 10: 'october', 11: 'november', 12: 'december'}

try:
    print(weekday[99])
except KeyError:
    print('A key error occured.')

print('values sequence is: ', weekday.values())
for day in sorted(weekday.values()):        # sift through all weekday values
    print(day)

print("keys sequence is:", weekday.keys(), "\n")
for day in sorted(weekday.keys()):
    print(weekday[day])


print('items sequence is:', weekday.items(), "\n")          # iterates through the loop
for key, value in weekday.items():
    print(key,value)

# tuple inside this loop, day is a tuple
print("BOP---------------")
for day in weekday.items():
    print(day)

    # this key does not exist, so the item will be added
weekday[8] = 'fiction'
print(weekday)

#tring to assign dicts with new values
weekday[8] = 'skipbop'
print(weekday, '\n')

# popitem returns and removes the last item (key:value pair as a tuple)
print("removing the pair: ", weekday.popitem())
print(weekday)

# attempt to eliminate the key 20
try:
    del weekday[20]
except KeyError:
    print("key does not exist")

# using pop with value 3 returns and moves entry
try:
    got_it = weekday.popitem(3)
    print("the popped value for key 3 is", got_it)
    print("new dictionary is", weekday)
except TypeError:
    print("that key does not exsist")

for (num, day) in weekday.items():
    if day == 'wedensday':
        print("the key for wedensday is", num)


# creating an inverse dictionary
backwards = {}
for num, day in weekday.items(): # .items returns tuples
    backwards[day] = num
print(backwards)

# the pickle library
try:
    # first open a file
    pick_file = open('pickled.dat', 'wb')
    # then save the dict to the file using d.dump()
    pickle.dump(weekday, pick_file)
    pickle.dump(months, pick_file)
    # close when finished
    pick_file.close()
    print("you got pickled")
except pickle.PicklingError:
    print("No pickles? :(")
except IOError:
    print("No pickles? :(")

# unpickling a file: ,must restore them in the SAME order
try:
    #open file in read binary mode
    pick_file = open('pickled.dat', 'rb')
    # multiple objects need to be loaded in opposite order they were dumped

    data_weekday = pickle.load(pick_file)
    data_month = pickle.load(pick_file)
    #close when done
    pick_file.close()

    print(data_weekday)
    print(data_month)
except pickle.UnpicklingError:
    print("no pickles?")

# grabs grade in neato order
grades = {(90,100): 'A', (80,90): 'B', (70,80): "c", (60,70): 'd', (0,60): 'F'}
score = 87
# loop grabs each value which is a tuple (start,end)
for (start,end) in grades:
    if score in range(start, end):
        print("\n for the score", score, "the letter in", grades[(start, end)])
