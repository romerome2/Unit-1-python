"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""
class Person:
    species = 'Homosapien'
    def __init__(self, name, age):
     self.name = name
     self.age = age
    def hi(self):
        print(self.name)
        print(self.age)

jerome = Person("Jerome", 16)
jerome.hi()

"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""
class Animal:
   def speak (self):
      print()

      class dog (Animal):
         def speak(self):
            print

"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""