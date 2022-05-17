import string
letter = 'a'
if letter in string.ascii_uppercase:
    print('true')
print(string.ascii_uppercase)

# strings can be manipulated like lists
word = 'mississippi'
print(len(word))

# access each individual letter using its index value
for index in range(len(word)):
    print("the leter at index", index, 'is', word[index])

word += ' river'
print(word)

try:
    word[12] = 'r'
except TypeError:
    print('strings are fun idk')




# slicing


word = 'mississippi'
print(word.isalpha())
print(word.isdigit())
print()
