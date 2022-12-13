#Create Dictionary list
super_villains = {'Fiddler' : ' Isaac Bowin',
                'Captain Cold' : 'Leonard Snart',
                'Weather Wizard' : 'Mark Mardon',
                'Mirror Master' : 'Sam Scudder',
                'Pied Piper': 'Thomas Perterson'}

# Print from list
print (super_villains['Captain Cold'])

#delete item from list
del super_villains['Fiddler']

#change value in Dictionary
super_villains['Pied Piper'] = 'Hartley Rathaway'

#number of items in Dictionary
print(len(super_villains))

#get vaule
print(super_villains.get("Pied Piper"))

#get list 
print(super_villains.keys())

#get list of dictionay values

print(super_villains.values())


