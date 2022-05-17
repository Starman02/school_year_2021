# ADD THIS LATER when doing pickles
import pickle  # open the pickle library

# defining a dictionary
weekday = {1: 'Sunday', 2: 'Monday', 3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday',
           7: 'Saturday'}
month = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July',
         8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

# simple loop
print("--- print the key and value for each weekday ---")
for key in weekday:
    print(key, weekday[key])

# count the entries (key:value pairs)
print("\nweekday has", len(weekday), "entries")

# look for value using a key of 5
print("\n--- print the value for key == 5, if found ---")
if 5 in weekday:
    print("The value for 5 is", weekday[5])

# try to access a value for a key that does not exist
print("\n--- attempt to access a key that does not exist ---")
try:
    print(weekday[99])
except KeyError:
    print("A KeyError occurred.")

# working with values
# since the .values() method returns a sequence, we can sort the result
print("\n--- working with the .values() method for weekday ---")
print("values sequence is:", weekday.values())

print("\n--- iterate through the sorted sequence of weekday.values() ---")
# sort the values alphabetically first
for day in sorted(weekday.values()):
    print(day)

# working with keys
print("\n--- working with the .keys() method for weekday ---")
print("keys sequence is:", weekday.keys(), "\n")
for day in sorted(weekday.keys()):
    print(day, weekday[day])

# working with items (returns key:value pairs as tuples)
print("\n--- working with the .items() method for weekday ---")
print("items sequence is:", weekday.items(), "\n")
# in this loop, day is a tuple
for day in weekday.items():
    print(day)

# the key,value tuple decomposes the tuple into separate variables
print("\n--- iterate through the weekday.items() sequence using a tuple in the for loop ---")
for key, value in weekday.items():
    print(key, value)

# this key does not exist, so the item will be added
print("\n--- when assigning a value to a key that doesn't exist, a new item is added to the dictionary ---")
weekday[8] = 'Fiction'
print(weekday)

# now that the key exists, its value will change
print("\n--- assigning a value to an existing key changes the existing value for the key ---")
weekday[8] = 'Fact'
print(weekday)

# use popitem to return AND remove the last item (key:value pair as a tuple)
print("\n--- .popitem() returns the last key, value pair and removes it from the dictionary ---")
print("Removing the pair:", weekday.popitem())
print(weekday)

# use del to delete a specific item
# if it does not exist it will generate a KeyError exception
print("\n--- attempt to elminate the key 20 using del ---")
try:
    del weekday[20]
except KeyError:
    print("key does not exist!")

# use pop to delete a specific item
# if it does not exist it will generate a KeyError exception
print("\n--- using pop with key value 3 returns and removes the entry ---")
try:
    got_it = weekday.pop(3)
    print("The popped value for key 3 is", got_it)
    print("Now the dictionary is", weekday)
except KeyError:
    print("key does not exist!")

# to find a key, we just use the subscript, but if I want to find a value
# need to loop through all of the items since the order of items is not guaranteed
print("\n--- one way to search for a value is to loop through all keys or key, value pairs ---")
for (num, day) in weekday.items():
    if day == 'Wednesday':
        print("The key for Wednesday is", num)

# sometimes it is helpful to create an inverse dictionary
# that uses the value as the key, and the key as value
# a loop is required to fetch the key, value pairs and add to the new dictionary
print("\n--- creating an inverse dictionary ---")
backwards = {}
for num, day in weekday.items():
    backwards[day] = num
print(backwards)

# pickling an object refers to storing and retrieving data while retaining the structure
# -- requires the pickle library
print("\n--- dump weekday and month to a data file, then re-load and display them ---")
try:
    # first, open a file in write-binary mode
    pickle_file = open('pickled.dat', 'wb')
    # then save the dictionary to the file using pickle.dump()
    pickle.dump(weekday, pickle_file)
    # you can dump multiple objects into one file
    pickle.dump(month, pickle_file)
    # close the file when finished
    pickle_file.close()
except pickle.PicklingError:
    print("No pickles for yffou!")
except IOError:
    print("No pickles for you!")

# unpickling means reading it back in -- if multiple objects are stored,
# you must restore them in the same order
try:
    # open in read-binary mode
    pickle_file = open('pickled.dat', 'rb')
    # multiple objects need to be loaded in the same order they were dumped
    data_weekday = pickle.load(pickle_file)
    data_month = pickle.load(pickle_file)
    # close the file when finished
    pickle_file.close()
    print(data_weekday)
    print(data_month)
except pickle.UnpicklingError:
    print("Oops! You got some bad pickles!")
except IOError:
    print("Where is the pickle jar?")

# Here is an example that uses tuples as the key
# by using the tuple values as the start and end of a range, a letter grade can be retrieved
grades = {(90, 101): "A", (80, 90): "B", (70, 80): "C", (60, 70): "D", (0, 60): "F"}
score = 87
# the for loop grabs each key which is a tuple (start, end)
# the corresponding value is a letter grade
for (start, end) in grades:
    # using the range() function, the start and end create a range of values
    if score in range(start, end):
        print("\nFor the score", score, "the letter grade is", grades[(start, end)],
              "because the score falls within the range", start, "to", end)
# if score in [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
