import random
import sys
import os

#list
grocery_list = ['Juice', 'water', 'potatoes',
             'bannas']

#print first item in list and override value
grocery_list[0] = "green Juice"
print ('First Item', grocery_list[0])

#print items 
print (grocery_list[1:3])

other_events = ['item1', 'item2', 'item3']

#combine two lists together
to_do_lists = [other_events,grocery_list]
print(to_do_lists)

#append items to list 

grocery_list.append('grapes')
print (to_do_lists)

#insert item in list 

grocery_list.insert(1, "Pickle")
print (to_do_lists)

#remove item in list 

grocery_list.remove("Pickle")
print (to_do_lists)

#sort

grocery_list.sort()

#reverse sort

grocery_list.reverse()

#delete item in list index 4 

del grocery_list[4]
print(to_do_lists)

#get length of lists

print(len(to_do_lists))