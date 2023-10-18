"""
Task 1: Calculate the Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""
def add_num(a):
    return a * a
x = add_num(10)
print(x)
assert add_num (10) == 100
assert add_num(5) == 25
# Asserterror if you get another answer and its not 100.

# I made a program that times the variable by it self to bet its answer

"""
Task 2: Calculate the Area of a Rectangle:
Write a function that takes the length and width of a rectangle and returns its area.
"""
def add_area(a,b):
    return a * b
x = add_area(12,4)
print(x)
assert add_area (12,4) == 48
assert add_area (13,3) == 39
# Basically in this function we just multiplied the variable value and got an answer.

"""
Task 3: Convert Temperature from Celsius to Fahrenheit:
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""
def con_cf(b):
    return b * 9 / 5 + 32
x = con_cf(95)
print(x)
assert con_cf(95) == 203.0

 # I made a program tha calculates the fahrenheit.
"""
Task 4: Calculate the Average of Numbers:
Write a function that takes a list of numbers 
and returns the average (mean) of those numbers.
"""