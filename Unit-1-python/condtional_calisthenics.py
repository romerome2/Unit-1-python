'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''
number1 = int(input("insert a number thank you"))
if number1 > 10 and number1 %2 == 0:
    print("true")
else:
    print("false")
    # i made a variable and i used the and to help determine if the statement was true or false.
'''

Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''
age = int(input("Enter your age"))
status = input("You a Student")
if age < 18 :
 print("Tickets cost 15$")

else:
    print("Tickets cost 20$")
# I made a program that tells wheter if your a student your tickets will be around 15 $ and if you are not a student then your tickets would be 20$
'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''
Fruit=["Banana, Apple, Strawberry, Avocado, Pineapple,"]
user=input("Give me a fruit:")
if user==Fruit:
   print("Yes, that fruit is in the list")
else:
   print("No that fruit is not in the list")
# This program just ask you to enter a fruit and if its not in the list then its wrong.

'''
Exercise 4:
Check if a year is a century year and a leap year.
'''
user=input("Enter the year :")
if int (user)%4==0 and int(user)%100 == 0:
   print("your year is a century and a leap year")
else:                    
   print("It's not a leap or a century year")
   # i made a program that tells you if its a leap year or not
'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''
weight=int(input("Enter the weight of the package"))
zone = input("please insert which zone you are shipping too")

'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''