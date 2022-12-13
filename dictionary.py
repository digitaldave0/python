def clear_my_screen():
  import os
  os.system('clear') 

clear_my_screen()
#dictonary 


my_car_dict = {
"brand": "Ford",
"model": "Focus",
"year": "2001",
"year": "2020"
}

 

print(my_car_dict) #dictonary will overwrite year with latest they are unordered
print(my_car_dict["brand"])
print(len(my_car_dict))
print(type(my_car_dict))
x = my_car_dict["model"]
print (x)
x = my_car_dict.keys()
print(x)
my_car_dict["colour"] = "red"
print(x)

x = my_car_dict.values()
print(x)

if "model" in my_car_dict:
  print ("model is one of the keys found")

#change year
my_car_dict = {
"brand": "Ford",
"model": "Focus",
"year": "2001",
"year": "2007"
}

my_car_dict["year"] = 2007
print (my_car_dict)

# print keys in dictionary
for x in my_car_dict:
  print(x)

# print items in dictionary
for x in my_car_dict:
    print(my_car_dict[x])

# use the vaules method to find values
for x in my_car_dict.values():
  print(x)

# use keys method 
for x in my_car_dict.keys():
  print(x)

# use items method
for x, y in my_car_dict.items():
  print(x, y)

# print all values in dictionary one by one
for x in my_car_dict:
  print(my_car_dict[x])

#copy dictionary create new 
new_dict = my_car_dict.copy()
print (new_dict)

#nested dictionary

mycars = {
  "model1" : {
    "brand" : "ford",
    "model" : "focus",
    "year"  : 1999
  },
  "model2" : {
    "brand" : "vw",
    "model" : "polo",
    "year" : 1976
  },
  "model3" : {
    "brand" : "seat",
    "model" : "ibiza",
    "year" : 2000
  }
}

for x in mycars:
  print(mycars[x])