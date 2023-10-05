"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""
name = 'Rome'
for t in name:
    print(t)

"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""
c=[2,1] # I created my varaibles
sum = 0
for e in c:
    sum+= e
    print(sum)
"""
Exercise 3:
Write a program to print the length of each word in a sentence using a for loop and a list.
"""
qwe='i like cats and dogs'
qwe = qwe.split(" ")
for we in qwe:
    print(we)
    print(len(we))
"""
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the resul

In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
"""
wp= {
   'apples':'banna',
   'cranberry':'chicken',
   'mouse':'cat',
    'add':'ears'
}
for x in wp:
    print (x)