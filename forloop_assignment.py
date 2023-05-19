#!/usr/bin/env python
# coding: utf-8

# 1. Do the following to create a program that simulates how websites ensure that everyone has a unique username.
# 
# * Make a list of five or more usernames called current_users.
# * Make another list of five usernames called new_users. Make sure one or 
#   two of the new usernames are also in the current_users list.
# * Loop through the new_users list to see if each new username has already been used. 
#   If it has, print a message that the person will need to enter a new username. 
#   If a username has not been used, print a message saying that the username is available.
# * Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted.

# In[ ]:


current_users = ['kate', 'michael', 'john', 'abby', 'hanna']
new_users = ['Kate', 'abby', 'lisa', 'janaka', 'patel']

for n_user in new_users:
    if n_user.lower() in [x.lower() for x in current_users]:
        print("enter a new username")
    else:
        print("username is available")
    


# 2. Color probability
# You're playing a game with a friend involving a bag of marbles. In the bag are ten marbles:
# 1 smooth red marble
# 4 bumpy red marbles
# 2 bumpy yellow marbles
# 1 smooth yellow marble
# 1 bumpy green marble
# 1 smooth green marble
# 
# You can see that the probability of picking a smooth red marble from the bag is 1 / 10 or 0.10 
# and the probability of picking a bumpy yellow marble is 2 / 10 or 0.20.
# 
# The game works like this: your friend puts her hand in the bag, chooses a marble (without looking at it) 
# and tells you whether it's bumpy or smooth. Then you have to guess which color it is before she pulls it
# out and reveals whether you're correct or not.
# 
# You know that the information about whether the marble is bumpy or smooth changes the probability
# of what color it is, and you want some help with your guesses.
# 
# Write a function color_probability that takes two arguments: a color ('red', 'yellow', or 'green') 
# and a texture ('bumpy' or 'smooth') and returns the probability of drawing that combination 
# as a decimal fraction accurate to two places.
# 
# The probability should be a string and should discard any digits after the 100ths place. 
# For example, 2 / 3 or 0.6666666666666666 would become the string '0.66'. 
# Note this is different from rounding.
# 
# As a complete example, color_probability('red', 'bumpy') should return the string '0.57'.

# In[12]:


def color_probability(color, texture):
    if texture == 'bumpy':
        if color == 'red':
            probability = 4/7
        elif color == 'yellow':
            probability = 2/7
        elif color == 'green':
            probability = 1/7
    else:
        if color == 'red':
            probability = 1/3
        elif color == 'yellow':
            probability = 1/3
        elif color == 'green':
            probability = 1/3
    result = "{:.2f}".format(probability)
    return result

print(color_probability('red', 'bumpy'))


# 3. Write an if-elif-else chain that determines a person’s stage of life.
# Set a value for the variable age, and then:
# * If the person is less than 2 years old, print a message that the person is a baby.
# * If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
# * If the person is at least 4 years old but less than 13, print a message that the person is a kid.
# * If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
# * If the person is at least 20 years old but less than 65, print a message that the person is an adult.
# * If the person is age 65 or older, print a message that the person is an elder.
# 
# 

# In[15]:


age = int(input("age: "))
if age < 2:
    print("baby")
elif age >= 2 and age < 4:
    print("toddler")
elif age >= 4 and age < 13:
    print("kid")
elif age >= 13 and age < 20:
    print("teenager")
elif age >= 20 and age < 65:
    print("adult")
else:
    print("elder")


# In[ ]:




