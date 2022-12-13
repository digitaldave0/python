import random
import sys
import os

#creating functions with python

def addNumber (fNum, lNum):
    sumNum = fNum + lNum
    return sumNum

#use function created above sunNum is only used in function
print(addNumber(1,4))

#using sys.stdin.readline we can read input 
print ('What is Your Name?')
name = sys.stdin.readline()
print('Hello',name)

def my_function():
  print("Hello from a function")
my_function()

def my_function_food(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function_food(fruits)