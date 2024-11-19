# Answer for Exercise 2

# Q1: Create a Python program that asks the user for their name, age, and country, then stores these in variables and displays a greeting message.
# Purpose: Collects user information (name, age, country) and displays a greeting message.
name = input("Enter your name: ")
age = input("Enter your age: ")
country = input("Enter your country: ")
# Prints a greeting message combining the collected data
print("Hello", name, "You are", age, "years old, from", country)

# Q2: Create a list of numbers
# Purpose: Create a list of numbers and compute their sum and average.
numbers = [12, 8, 15, 7, 10]

# Calculate the sum and the average of the numbers
# Computes the total sum
total_sum = sum(numbers)
# Computes the average by dividing the total sum by the length of the list
average = total_sum / len(numbers)

# Print the sum and average
print('List of the number: ', numbers)
print("Sum of numbers:", total_sum)
print("Average of numbers:", average)

# Q3: Create a 3x3 matrix using lists
# Purpose: Create a 3x3 matrix and print each row.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Print each row of the matrix
for row in matrix:
    print(row)

# Q4: Creates a 2x2 matrix using lists, and prints each row of the matrix on a new line.
# Purpose: Create a 2x2 matrix and print each row, along with specific elements.
matrix2 = [[1, 2], [3, 4]]

# Prints each row in the matrix
for row in matrix2:
    print(row)

# Prints specific elements: top left (0,0) and bottom right (1,1)
print("Top left", matrix2[0][0])
print("Bottom right", matrix2[1][1])
