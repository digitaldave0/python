info = {
    "Firstname": "jsdkjdsk",
    "Surname": "dsjksjdk",  
}
try:
    print(info['Firstname'])
except KeyError as e:
    print ("You tried to enter a key that does not exist?")
    print (f'Key: {e}')
else:
    print("it worked")
finally:
    print("finished")
