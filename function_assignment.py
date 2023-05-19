#!/usr/bin/env python
# coding: utf-8

# 1. Finding Prime Number
# 
# A prime number is an integer greater than one that is only divisible by one and itself. Write a function that determines whether or not its parameter is prime, returning True if it is, and False otherwise. Write a main program that reads an integer from the user and displays a message indicating whether or not it is prime.

# In[20]:


def is_prime(number):
    if number % 2 == 0:
        return False
    for x in range(number):
        if number%(x+1) == 0 and number != 1: #x+1 because of 'divison by zero'
            return True
        else:
            return False


user_input = int(input("Enter a number: "))
print(is_prime(user_input))
    


# 2. Rømer temperature
# 
# You're writing an excruciatingly detailed alternate history novel set in a world where Daniel Gabriel Fahrenheit was never born.
# 
# Since Fahrenheit never lived the world kept on using the Rømer scale, invented by fellow Dane Ole Rømer to this very day, skipping over the Fahrenheit and Celsius scales entirely.
# 
# Your magnum opus contains several thousand references to temperature, but those temperatures are all currently in degrees Celsius. You don't want to convert everything by hand, so you've decided to write a function, celsius_to_romer that takes a temperature in degrees Celsius and returns the equivalent temperature in degrees Rømer.
# 
# For example: celsius_to_romer(24) should return 20.1.

# In[22]:


def celcius_to_romer(deg):
    return (deg * 21/40) + 7.5

print(celcius_to_romer(24))


# 3. Pixelart planning
# 
# You're laying out a rad pixel art mural to paint on your living room wall in homage to Paul Robertson, your favorite pixel artist.
# 
# You want your work to be perfect down to the millimeter. You haven't decided on the dimensions of your piece, how large you want your pixels to be, or which wall you want to use. You just know that you want to fit an exact number of pixels.
# 
# To help decide those things you've decided to write a function, is_divisible that will tell you whether a wall of a certain length can exactly fit an integer number of pixels of a certain length.
# 
# Your function should take two arguments: the size of the wall in millimeters and the size of a pixel in millimeters. It should return True if you can fit an exact number of pixels on the wall, otherwise it should return False. For example is_divisible(4050, 27) should return True, but is_divisible(4066, 27) should return False.
# 
# Note: you don't need to use an if statement here. Remember that in Python an expression using the == comparison operator will evaluate to either True or False:

# In[25]:


def is_divisible(wall, pixel):
    return wall % pixel == 0 
print(is_divisible(4050, 27))
print(is_divisible(4066, 27))


# In[ ]:




