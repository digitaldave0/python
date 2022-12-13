#list constructor

my_list = list(("ford","vauxhall","bmw","mazda","Renault ")) # create list with constuctor
print (my_list) # print created list

 

my_car_list = ["ford","vauxhall","bmw","mazda","Renault"] # create dictionary list
print (my_car_list[-1]) # last item in list "renualt"
print (my_car_list[0:3]) # range index "ford, "vauxhall" and "bmw"

#check if item in list exists

if "bmw" in my_car_list:
    print ("Yes, 'bmw is in the list")

#Change item in my_car_list

my_car_list[4] = "Peugeot"
print(my_car_list) # swap "Renault" for "peugeot"


#replace one value with two

my_car_list[1]= ("vw","jaguar") #replace vauxhall with vw and jaguar
print(my_car_list)

#insert items in list

my_car_list.insert(3,"landrover")
print (my_car_list)

#append to list

my_car_list.append("seat")
print(my_car_list)

#extend list with new items in other list

my_car_list_updates = ["audi","citroen","honda"]
my_car_list.extend(my_car_list_updates)
print(my_car_list)
 
my_car_list.remove("citroen")
print(my_car_list)  # remove citroen from list

my_car_list.pop(1)
print(my_car_list) # remove 2nd item from list

my_car_list.pop()
print(my_car_list) # remove last item from list honda

#delete entire list
#del my_car_list


#clear the list content
my_car_list.clear()
print (my_car_list) # list remains but no items in list.

#loop through items in my_car_list

my_car_list = ["ford","vauxhall","bmw","mazda","Renault","audi"] # reload my_car_list after clear
for x in my_car_list:
  print (x.capitalize())

#loop through index numbers
for i in range(len(my_car_list)):
    print([i])
 
#while loop all index numbers in dictionary
i = 0 # start at 0
while i < len(my_car_list): # while length of my_car_list is higher than 0
  print(my_car_list[i]) # print the value of item in my_car_list
  i = i + 1  # increment by 1 and continue until you reach my_car_list length
 
#list comprehension

[print(x) for x in my_car_list]

#create new list if bmw is in original list with bmw in it

my_car_list = ["ford","vauxhall","bmw","mazda","Renault","audi"]
new_list = [x.upper() for x in my_car_list if "bmw" in x]
print (new_list)

#sort lists

my_car_list.sort()
print(my_car_list) 

#descending
my_car_list.sort(reverse=True)
print(my_car_list)

#case-insensative sort
my_car_list.sort(key = str.lower)
print(my_car_list)

#reverse

my_car_list.reverse()
print(my_car_list)

#copy lists copy list to my_new_car_list
my_new_car_list = my_car_list.copy()
print(my_new_car_list)

#join two lists
joined_car_lists = my_car_list + my_car_list_updates
print(joined_car_lists)