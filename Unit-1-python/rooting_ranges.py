"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""
print("numbers from 1 to 10")
for x in range(10):
      print(x)
# I created a for loop that had made a number go up to a specific number range.
"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""
for x in range (900,1001,10):
      print(x)
     # I created a for loop that had a range count by 10s .
"""
Exercise 3:
Write a program that counts form 1-100 by 9
"""
for x in range (0,100,9):
      print(x)
      # I created a range that counts from 1- 100 by 9.
"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""
for x in range (1,11):
     total = 0
total += x
print(total)
# I just made a for looop and used the range to help make a sum of all numbers from 1 to 10.
"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?

- Explain the iterative process that this code executes to get that output
"""
rows = 5
for i in range(rows):
    for j in range(i + 1):
        print('*', end=' ')
    print()
    # The output of the program was stars. I think the code was to add the numbers by 1 and to keep counting after you added by 1.