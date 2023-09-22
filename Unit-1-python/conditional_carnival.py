'''
TASK 1 Even or Odd
Determine if a number is even or odd.
'''
num=int(input("Enter a number to see if it's odd or even"))
if (num % 2) == 0:

              print ("its even")
else:
         print("The number is odd")                 
# I made my code check to see if the code was right by using the if and else statement.
'''
TASK 2 Positive, Negative, or Zero:
Determine if a number is positive, negative, or zero.

'''
c=int(input("what is the number"))
if c > 0:
    print("postive")
elif c < 0:
    print("negative")# I made a variable which was c 
'''
TASK 3: Largest of Three
Find and print the largest of three numbers.
'''
a=[1,2,3]
b=max(a)
print(b)
# I made a variable then i wrote a number and made it max out at 3 so it made the answer 3
'''
TASK 4: Leap Year
Determine if a year is a leap year or not.
'''
BirthYear =int(input("please insert your birth year"))
if BirthYear % 4 == 0:
        print("Congraulations,you were born on a leap year")5

else:
        print("Sorry, you were not born on a leap year")
'''
TASK 5: Vowel or Consonant:
Identify if a character is a vowel or consonant.

EXTRA CREDIT: Tell the user if they did not enter a valid letter
'''
ch = input("Enter a character: ")

if(ch=='A' or ch=='a' or ch=='e' or ch=='E' or ch=='I' or ch=='i'
   or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
        print(ch,"is a vowel")
else:
        print(ch,"is a Consonant")
        