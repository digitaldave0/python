import random
import sys
import os

#create class __ means private
class Animal:
    __name = ""
    __height = 0
    __weight = 0
    __sound = 0

#constr

def __int__(self, name, height, weight, sound):
    self.__name = name
    self.__height = height
    self.__weight = weight
    self.__sound = sound

#set vaules for object 

def set_name(self, name):
    self.__name = name

def set_height(self, height):
    self.__height = height 

def set_weight(self, weight):
    self.__weight = weight

def set_sound(self, sound):
    self.__sound = sound
    

#get values for object

def get_name(self):
    return self.__name

def get_height(self):
    return self.__height

def get_weight(self):
    return self.__weight

def get_sound(self):
    return self.__sound

def get_type(self):
    print("Animal")

def toString(self):
    return "{} is {} cm tall and {} kilogramms and says {}".format(self.__name,
                                                                   self.__height,
                                                                   self.__weight,
                                                                   self.__sound)
cat = Animal('Whiskers',33,10, 'Mellow')
print(cat.toString())





