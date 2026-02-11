#Function Without Parameters
# Create a function that:
#  Takes no parameters
#  Uses arithmetic operators to calculate the area of a rectangle
#  Prints the result

def rectanglearea():
    length = int(input("Enter length: "))  # Define the length
    width = int(input("Enter width: "))    # Define the width
    area = length * width  # Calculate the area
    print(f"The length is: ",length) 
    print(f"The width is: ", width)
    print(f"The area of the rectangle is: ", area)
rectanglearea()
print("==============================")


# Create a function that:
# Accepts two numbers as parameters
# Returns their sum, difference, product, and division

def calculate_arithmetic():
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    sum = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    quotient = num1 / num2
    print("The sum is: ", sum)
    print("The difference is: ", difference)
    print("The product is: ", product)
    print("The quotient is: ", quotient)
calculate_arithmetic()
print("==============================")


# Write a function that:
# Accepts a number (use input function)
# Checks whether the number is:
# Positive
# Negative
# Zero

def number():
    
# 1. Accept a number using the input function
    number = float(input("Enter a number: "))

# 2. Check the status using if...elif...else
    if number > 0:
        print(f"The number {number} is Positive.")
    elif number < 0:
        print(f"The number {number} is Negative.")
    else:
        print(f"The number {number} is Zero.")
number()
print("==============================")


# Write a function that:
# Accepts a number n
# Uses a for loop
# Calculates the sum of numbers from 1 to n

def calculate_sum_to_n(n):
    sum = 0
    # Uses a for loop to iterate through the range of numbers from 1 to n+1
    # range(1, n + 1) generates numbers starting at 1 and stopping BEFORE n + 1
    for number in range(1,n+1):
        sum +=number  # Adds the current number to the running total
    print("The sum of numbers from 1 to",n,"is:",sum)
n = int(input("Enter a number:"))
calculate_sum_to_n(n)
print("==============================")




# Write a function that:
# Accepts a number (Use input() function)
# Uses a while loop
# Calculates the square of numbers from 1 up to that number

def calculate_squares(n):
    i = 1
    while i<=n:
        square = i**2
        print("The square of",i,"is:",square)
        i+=1
n = int(input("Enter a number:"))
calculate_squares()
print("==============================")


