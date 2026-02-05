# Python Lists
# A list inpython is a collection of items that are ordered in a certain way.
# A list is introduced by the use of the square brackets []
# The items of a list are stored inside of indexes. NOTE: In programming we start counting from index Zero(0). bmw, benze, hiance, ...
# A list is mutable i.e the contents of a list can be changed.

cars = ["BMW", "Benze", "Hiance", "Prado", "Probox", "McLaren", "Range"]

print(cars)
print(type(cars))

# Accessing items of a list
print(cars[2])
print("The car on index four is: ", cars[4])

# List slicing - This is creating a list from a given bigger list
print(cars[4:])

# printing from index zero to index three
print(cars[:4])


# printing from Hiance to Probox
print(cars[2:5])

# List - Mutability
# we use the function append to add an item at the end of a list
cars.append("Mercedes")
print(cars)

cars.append("Subaru")
print(cars)

# we use the pop function to remove an item at the end of the list.
cars.pop()
print(cars)

# we can use an index to add items to a list
cars[5] = "Pajero"
print(cars)

# we can use the sort function to sort out items in alphabetical order
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

del cars[4]
print(cars)
cars.pop(4)
print(cars)
cars.remove("BMW")
print(cars)