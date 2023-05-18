#!/usr/bin/env python
# coding: utf-8

# In[7]:


""" 1- Ask the user to enter a number between 10 and 20 (inclusive). 
If they enter a number within this range, display the message “Thank you”, 
otherwise display the message “Incorrect answer”. """
num = int(input("Enter a number between 10 and 20: "))
if num >= 10 and num <= 20:
    print("Thank You")
else:
    print("Incorrect answer")


# In[12]:


""" 2- In this exercise, you will create a program that reads a letter of the alphabet from the user. 
According to the answer:

-- If the user enters a, e, i, o, u, then your program should display a message indicating 
   that the entered letter is a vowel.
-- If the user enters y, then your program should display a message indicating that y is 
   sometimes a vowel and sometimes a consonant.
-- Otherwise, your program should display a message indicating that the letter is a consonant."""

letter = input("Enter a char: ")
if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
    print(letter, "is vowel")
elif letter =='y':
    print(letter, "is sometimes a vowel and sometimes a consonant ")
else:
    print(letter, "is a consonant")


# In[ ]:




