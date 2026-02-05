# 1. Write a python program that is able to calculate the BMI of a person whose weight is 78kgs and height is 1.75 meters. BMI = (weight) / (height squared)
weight = 78
height = 1.75
BMI = (weight) / (height)
print("The BMI of a person is: ", BMI)
print(type(BMI))

# 2. Find the Area and perimeter of a rectangle whose length is 48cm and width is 25cm
length = 48
width = 25
Area = (length * width)
print("The area of the rectangle is: ", Area)
print(type(Area))

length = 48
width = 25
Perimeter = length + width
print("The area of the rectangle is: ", Perimeter)
print(type(Perimeter))

# Research on python list, tuple and Dictionary Data types.

#  These are  pythons built-in data types for collections each with distinct characteristics in regards to its order, mutability, and how data is accessed. 

#LIST
#A list is a mutable, ordered collection of items that allows duplicate members. Items are stored in a specific sequence and can be accessed by their position (index), starting from zero. 
Characteristics: # Ordered, Changeable (mutable), Allows duplicate members, Indexed.
Syntax: # Defined using square brackets [].
Example: # shopping_list = ["apple", "banana", "cherry", "apple"].
Use Case: #Ideal for dynamic collections where elements will be frequently added, removed, or modified. 
#TUPLE
#A tuple is an immutable, ordered collection of items that also allows duplicate members. Once a tuple is created, its contents cannot be changed (elements cannot be added, removed, or modified). 
Characteristics: Ordered, Unchangeable (immutable), Allows duplicate members, Indexed.
Syntax: #Defined using round parentheses ().
Example: #coordinates = (10.0, 20.0).
Use Case: #Used for data that should remain constant throughout the program's execution, such as coordinates or configuration settings. Tuples can also be used as dictionary keys, which lists cannot. 
#DICTIONARY
#A dictionary is a mutable collection that stores data in unique key:value pairs. It is designed for efficient data retrieval by key, rather than by numerical index. As of Python 3.7, dictionaries are ordered. 
Characteristics: #Ordered (as of Python 3.7), Changeable (mutable), Keys must be unique and immutable, Values can be of any type.
Syntax: #Defined using curly braces {} with key-value pairs separated by colons.
Example: #user_info = {"name": "Alice", "age": 30}.
Use Case: #Excellent for mapping data (like a phonebook maps names to numbers) or representing structured records where you want to access data by a specific name or identifier instead of a position. 