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


# Write a function that:
# Accepts a number n
# Uses a for loop
# Calculates the sum of numbers from 1 to n

def calculate_sum_to_n(n):
    
    total_sum = 0
    # Uses a for loop to iterate through the range of numbers from 1 to n+1
    # range(1, n + 1) generates numbers starting at 1 and stopping BEFORE n + 1
    for number in range(1, n + 1):
        total_sum += number  # Adds the current number to the running total

    print(total_sum)

# Example Usage:
# Calculate the sum of numbers from 1 to 5 (1 + 2 + 3 + 4 + 5 = 15)
result_5 = calculate_sum_to_n(5)
print(f"The sum of numbers from 1 to 5 is: {result_5}")

# Calculate the sum of numbers from 1 to 100
result_100 = calculate_sum_to_n(100)
print(f"The sum of numbers from 1 to 100 is: {result_100}")




# Write a function that:
# Accepts a number (Use input() function)
# Uses a while loop
# Calculates the square of numbers from 1 up to that number

def calculate_squares():
    """
    Calculates the square of numbers from 1 up to a user-specified number.
    """
    # 1. Accept a number from the user
    user_input = input("Enter a positive integer: ")
    limit = int(user_input)
        
    if limit < 1:
        print("Please enter a positive integer.")
    else:    
        print("Invalid input. Please enter a whole number.")

    # Initialize a counter variable
    current_number = 1

    print(f"Squares from 1 to {limit}:")

    # 2. Use a while loop
    while current_number <= limit:
        # 3. Calculate the square of the current number
        square = current_number ** 2
        print(f"The square of {current_number} is {square}")
        
        # Increment the counter to move to the next number
        current_number += 1

# Call the function to run the program
calculate_squares()


