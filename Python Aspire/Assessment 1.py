"""1. Answer these 3 questions without typing code. Then type a code to check your answer.
What is the value of the expression 4 * (6 + 5)
44
What is the value of the expression 4 * 6 + 5
29
What is the value of the expression 4 + 6 * 5
34
2. What would you use to find a number’s square root, as well as its square?
3.
Try creating your own variables and storing values into those variables.
Print out the values that are stored and print the datatype of the variables created.


4.
Include an assignment that will add two numbers together (for example 4+5) and then assign the result to a variable.
Similarly perform all the mathematical operations like Subtraction, Multiplication, Division, floor division , Power,
Square root and print out that variables value once it has been assigned a value
5. Try Printing “*” - in the first line 20 times , second line 30 times and third row 40 times
6. Try out Examples with various Expression consisting of multiple operators.
"""
import math

# print(math.factorial(4))
print(4 * (6 + 5))
print(4 * 6 + 5)
print(4 + 6 * 5)

# to find square or square root we can use functions


# Find the square root
sqrt_result = math.sqrt(9)

# Find the square
square_result = 3 ** 2

print("The square root of 9 is:", sqrt_result)
print("The square of 3 is:", square_result)

# creating variables and finding datatypes
a = 5
b = 'a'
d = 0
e = [1, 2, 3, 4, 5, 6, 7, 8, 9]
c = 3.14
f = ["Wonderful Day"]

print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(d))
print(e)
print(type(e))
print(f)
print(type(f))

# Calculator
a = 2
b = 3

# Addition
addition_result = a + b
print("Addition result 2 & 3:", addition_result)

# Subtraction
subtraction_result = b - a
print("Subtraction result 2 & 3:", subtraction_result)

# Multiplication
multiplication_result = a * b
print("Multiplication result 2 & 3:", multiplication_result)

# Division
division_result = b / a
print("Division result 2 & 3:", division_result)

# Floor Division
floor_division_result = b // a
print("Floor Division result 2 & 3:", floor_division_result)

# Power
power_result = b ** a
print("Power result (3^2):", power_result)

# Square Root
square_root_result = math.sqrt(power_result)
print("Square root result (√power_result):", square_root_result)

# * print

lines = [20, 30, 40]

# Use a for loop to print "*" the specified number of times
for count in lines:
    print("*" * count)

# multiple operator examples
#  Arithmetic operators
result_1 = (5 + 3) * 4 - 2 ** 2 / 2
print("Result of expression 1:", result_1)

#Combination of arithmetic and comparison operators
result_2 = (10 - 3) > 2 and (2 * 3) <= 6
print("Result of expression 2:", result_2)

# Use of parentheses to change precedence
result_3 = 10 - (3 > 2) * (1 + 2)
print("Result of expression 3:", result_3)

# Logical operators with comparison
result_4 = not (5 == 3) and (3 < 6 or 7 > 8)
print("Result of expression 4:", result_4)

#Modulus and floor division operators
result_5 = 25 % 4 + 25 // 4
print("Result of expression 5:", result_5)
