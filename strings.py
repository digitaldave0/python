import random
import sys
import os

long_string = "the quick brown fox jumps over the lazy dog"

#print first 4 char
print(long_string[0:4])

#last 5 chars
print(long_string[-5:])

#all chars expect last 5
print(long_string[:-5])

#read first 9 chars and append with mouse
print(long_string[:9] + "mouse")

#formating with %c char, %s string, %d decimal %f float

print("%c is the first letter in %s and is number %d in the alphabet %f " % ('C','Cheese',3,1.4))

#capitalize firt letter of string
print (long_string.capitalize())

#find the postion in string for the vaule fox
print(long_string.find('fox'))

#check string is alpha
print(long_string.isalpha())

#check string is num
print(long_string.isalnum())

#print the len of the string 
print (len(long_string))

#replace fox with cat
print (long_string.replace("fox","cat"))

#strip whitespace 
print (long_string.strip())

#split string into list 
quote_list = long_string.split(" ")
print (quote_list)
