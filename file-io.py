import random
import sys
import os

#open a file called fileio.txt

test_file =open('fileio.txt', "wb")

#print its file mode
print(test_file.mode)

#print the filename
print(test_file.name)

#write an entry to file and close
test_file.write(bytes("Write this to the file\n"))
test_file.close()

#open the fileio.txt and read contents
test_file = open('fileio.txt', "r+")
text_in_file = test_file.read()
print(text_in_file) 

#remove fileio.txt
os.remove("fileio.txt")