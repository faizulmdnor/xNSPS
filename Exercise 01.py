# Addition
from numpy.random.mtrand import operator

a = 10
b = 5
sum_result = a + b
print("Sum:", sum_result)

# Subtraction
sub_result = a - b
print("Difference:", sub_result)

# Multiplication
mul_result = a * b
print("Product:", mul_result)

# Division
div_result = a / b
print("Quotient:", div_result)

# Modulus (remainder of the division)
mod_result = a % b
print("Remainder:", mod_result)

'''
Exercise: Even or Odd Checker
Write a Python program that checks if a given number is even or odd.

Prompt the user to enter a number.

Check if the number is even or odd.

Print the result.
'''

try:
    number = int(input('Masukan integer: '))
    if number % 2 == 0:
        print(f'{number} adalah nombor Genap')
    else:
        print(f'{number} adalah nombor Ganjil')
except Exception as e:
    print(f'Masukan nombor integer sahaja! {e}')

'''
Exercise: Simple Calculator
Create a Python program that takes two numbers and an operator from the user and performs the corresponding operation.

Prompt the user to enter two numbers.

Prompt the user to enter an operator (+, -, *, /).

Perform the operation based on the operator.

Print the result.
'''

# input

num1 = float(input('Masukan angka pertama: '))
num2 = float(input('Masukan angka kedua: '))
operator = input('Masukan operator (+, -, *, /): ')

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2
else:
    result = 'Operator tidak dapat dikenali'
print(f'{num1} {operator} {num2} = {result}')


