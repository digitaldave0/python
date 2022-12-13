#create file 
f = open("demofile.txt")

#create file read for text
f = open("demofile.txt","rt")

#open file and read lines
f = open("demofile.txt", "r")
print(f.read())

#open a file in a different folder
f = open("c:\\myfiles\welcome.txt", "r")
print(f.read())

#read first five chrs of file
f = open("demofile.txt", "r")
print(f.read(5))

#read one line of file
f = open("demofile.txt", "r")
print(f.readline())

#loop file line by line
f = open("demofile.txt", "r")
for x in f:
  print(x)

#close file after writing
f = open("demofile.txt", "r")
print(f.readline())
f.close()

#append content to file
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

#open file write file 
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())

#create new file
f = open("myfile.txt", "x")

#create new file if it doesn't exist
f = open("myfile.txt", "w")

#remove file
import os
os.remove("demofile.txt")

#check if it exists then delete

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

#delete folder

import os
os.rmdir("myfolder")

