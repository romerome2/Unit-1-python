# Task 1: Greeting Function
# Write a function `greet(name)` that takes a name as a parameter and prints a greeting message like "Hello, [name]!".
def my_function(name):
    print("Hello" + name)
my_function("Rome")
# Basically my function prints hello with my name

# Task 2: Sum of Two Numbers
# Write a function `sum_numbers(a, b)` that takes two numbers as parameters and returns their sum.
def sum_numbers(a,b):
    print(a + b)
sum_numbers(40,10)
    # I made a program that adds a and b that has intergers together so all the computer had to do was add them up.

# Task 3: Calculate Factorial
# Write a function `factorial(n)` that calculates the factorial of a given number `n`.
def factorial(n):
    ab = 1
    while n > 1:
        ab = n * ab
        n = 1 
    print(ab)
factorial(9)
# The program basically factors out a number.

# Task 4: Check Even or Odd
# Write a function `is_even(num)` that takes a number as a parameter and returns `True` if the number is even, and `False` otherwise.
def is_even(num):
    if num % 2 ==0:
        print('True')
    else:
        print('False')

# Task 5: Calculate Area of a Rectangle
# Write a function `calculate_area(length, width)` that calculates and returns the area of a rectangle given its length and width.
def calculate_area(length, width):
    n = length * width
    print(n)
calculate_area(32,15)