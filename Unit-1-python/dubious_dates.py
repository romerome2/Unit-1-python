import datetime
"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""
today=datetime.datetime.now()
print(today)
# The code will print out time of today

"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""
today = (datetime.datetime.now())
print(today.strftime('%m/%d/%y %h:%m:%s'))
# THE CODE WILL PRINT OUT TODAYS DATE.
"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""
str_d1 = "03 15 2023"
str_d2 = "03 12 2023"

date_format ="%M %d %Y"
date1 = datetime.datetime.strptime(str_d1, date_format)
date2 = datetime.datetime.strptime(str_d2,date_format )

difference = (date2 - date1).days

print("The difference is", difference,"days")
# The point of this code was to convert my strings to a date.
"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""

