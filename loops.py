
#loops

#for loop starting at 0 - 9
for x in range(0,10):
    print ("-""\n")

#newline
print('\n')

#create list and loop through
grocery_list = [' ', 'water', 'potatoes',
             'bannas']
for y in grocery_list:
    print(y)

#loop from 2 - 10
for x in [2,4,6,8,10]:
    print(x)

#loops within loops
num_list =[[1,2,3],[10,20,30],[100,200,300]]

#loop through string 

for x in "banana":
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


for x in range(6):
  print(x)
else:
  print("Finally finished!")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)