import random
import sys
import os

# statements if else elif

age = 30 

if age > 16 :
    print('You are old enough to drive')
else :
    print('You are not old enough to drive')

if age >=21 :
    print ('You are old enough to drive a tractor')
elif age >= 16 :
    print ('You are old enough to drive a car')
else :
    print ("You are no old enough to drive")

#logical operators and or not

if ((age >=1) and (age <=18)):
    print("You get a brithday")
elif (age == 21) or (age >=65):
    print("Yout get a brithday")
elif not (age == 30):
    print("You don't get a birthday")
else:
    print("You get a birthday party")

    
