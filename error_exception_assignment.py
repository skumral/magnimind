#!/usr/bin/env python
# coding: utf-8

# 1- Let us define a division operation inside a function (using def) but to get an error, define the denominator as 0. So, type except statement properly.
# 

# In[3]:


def div(num):
    divisor = 0
    try:
        num / divisor
    except:
        print("ZeroDivisionError")
        
div(9)
    


# 2- It is possible to get multiple errors after the execution of one try block. So, please define an error-exception issue with NameError.
# 

# In[7]:


number = 10
try:
    print(num*2)
except: 
    print("NameError")


# 3- Please define a function and with this function, generate a ValueError exception simply by entering a string instead of numerical value.
# 

# In[17]:


def func_value_error():
    number = input("enter a number: ")
    try:
        total = number + 3
    except:
        print("ValueError")

func_value_error()


# 4- Write a function called circumference that takes the diameter of a circle as input and produces the circumference of the circle. Your function should use try...except to check for a type error in the event a string is passed.
# 

# In[21]:


def circumference(diameter):
    try:
        result = 2 * 3.14 * (diameter / 2)
        return result
    except:
        print("TypeError: diameter must be numerical value")
        
circumference("abc")
print(circumference(9))


# In[ ]:




