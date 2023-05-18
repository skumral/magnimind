#!/usr/bin/env python
# coding: utf-8

# In[9]:


"""1- Create a dictionary with 7 days. Ask the user to choose 2 different days by listing 
      the (e.g. "12" for Monday and Tuesday). Delete the user-selected days from the dictionary 
      and print the remaining 5 days on the screen. """
 
week = {'1': 'monday', '2': 'tuesday', '3': 'wednesday', '4': 'thursday', '5': 'friday', '6': 'saturday', '7': 'sunday'}
day1, day2 = input("pick two days: ")
week.pop(day1)
week.pop(day2)
print(week)


# In[12]:


"""2- Create a dictionary with the following personnel. Use names as keys.
      (Michael (age: 20)
      (Linda (age: 30) """
personnel = {'Michael': {'age': 20}, 'Linda': {'age': 30}}


# In[14]:


"""3- Add child information to Michael and Linda. 
      Michael has two children (Karen (age : 12, female) and 
      Greg (age : 7, male) and 
      Linda has one child (Susan (age: 6, female) """
personnel['Michael'] = {'age': 20,
                        'Karen': {'age': 12,
                                  'gender': 'female'}, 
                        'Greg': {'age': 7,
                                 'gender': 'male'}}
personnel['Linda'] = {'age': 30,
                      'Susan': {'age': 6,
                                'gender': 'female'}}
                   


# In[18]:


""" 4- Print the names of Michael's children in a list."""
child_list = list(personnel['Michael'].keys())[1:]
print(child_list)


# In[ ]:





# In[ ]:




