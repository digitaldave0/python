import random
import sys
import os

#create a random number within range
random_num = random.randrange(0,100)

#while random_num is not 15 keep looping
while(random_num !=15):
    print(random_num)
    random_num = random.randrange(0,100)

#Using while with break and continue
i = 0;

while (i <= 20):
    if (i%2 == 0):
        print(i)
    elif (i == 9):
        break
    else:
        i +=1
        continue
    i +=1

