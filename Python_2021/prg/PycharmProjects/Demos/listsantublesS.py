dogs = ["shepard", "Collie", "crack", "corgi", "five", "ford"]

print(dogs)

print("first three dogs using [:3]:", dogs[:3])  # same as [0:3]
print("last three dogs using [-3:]:", dogs[-3:])  # same as [0:3]

# print one line at a time
for dog in dogs:
    print(dog, 'dawg')

#   get the middle value
middle = len(dogs) // 2
print(dogs[middle - 1: middle + 2], 'are in the middle')

print("\nchanging the dog at index 3 tp weimarner")
dogs[3] = 'weinmarnernerner'
print(dogs)

#inserting
dogs.insert(3, 'boog')

print('\nboog was found at index', dogs.index('boog'))

if 'ford' in dogs:
    print('\nsi ford was found')
else:
    print("no ford :(")

#   repitition
values = [0] * 6
print(values)


# multiple data types
lista = ['a', 'b', 'c']
listb = [1, 2, 3]
listc = lista + listb
print(listc)

#   append demo
dogs.append("squidward")
for index in range(len(dogs)):
    print(index + 1, dogs[index])
print("___________________________________")

print("min value with min():", min(dogs))
print("maximum value with min():", max(dogs))

#   sort the dogs
dogs.sort()
index = 0
while index < len(dogs):
    print(index + 1, dogs[index])
    index += 1

print("reverse reverse")
dogs.reverse()
for index in range(len(dogs)):
    print(index + 1, dogs[index])

print("\ncount the dogs with len():", len(dogs))
print("\npriint the third dawg:", dogs[2])


#   lists within lists
matrix = [[1, 2, 3], [4, 5, 6], [323, 43, 4]]
print(matrix)
print('matrix[0] is', matrix[0])
print("matrix[0][0] is", matrix[0][0])


# use a nested list to deal with nested lists
for outer in matrix:
    print(outer)
    for inner in outer:
        print(inner)




# i have 2 variabes
a = 'b'
b = 'sasquatch'
print(a,b)

a = b
b = a
print("after assighn", a, b)
a = 7
b = 5


(a, b) = (b, a)
print("after swap a:", a, "b", b)

def tuple_example():
    name = 'john'
    id_number = 27
    return name, id_number                  # returns tuple



(student, studentid) = tuple_example()
print(student)
print(studentid)

