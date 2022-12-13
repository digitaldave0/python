#create class 

class MyClass:
  x = 5

#create an object named p1, and print the value of x:
p1 = MyClass()
print(p1.x)

"""The __init__() Function
The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

To understand the meaning of classes we have to understand the built-in __init__() function.

All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
"""

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

print(p1.name)
print(p1.age)

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

def greeting(name):
  print("Hello, " + name)

import platform
x = platform.system()
print(x)

import platform
x = dir(platform)
print(x)
