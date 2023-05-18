#!/usr/bin/env python
# coding: utf-8

# In[7]:


#1- Write a code to compute the sum of the two lowest numbers and the two highest numbers in the following list.

my_list = [34, 56, 76, 45, 2, 12, 67, 98, 37, 54, 66]
my_list.sort()
sum = my_list[0] + my_list[1] + my_list[-1] + my_list[-2]
print(sum)


# In[18]:


#2- The following two lists contain student names and scores. Write a code that 
#   gets the name from the user and prints the score of that student.

names = ["David", "Michael", "John", "James", "Greg", "Mark", "William", "Richard", "Thomas", "Steven",  
         "Mary", "Susan", "Maria", "Karen", "Lisa", "Linda", "Donna", "Patricia", "Debra", "Eric"]
scores = [99, 87, 78, 86, 68, 94, 76, 97, 56, 98, 76, 87, 79, 90, 73, 93, 82, 69, 97, 98]


user_name = input("user name:")
score_index = names.index(user_name)

print(scores[score_index])


# In[41]:


#3- By using the two lists above, what is the maximum score and how many students got that score?
scores = [99, 87, 78, 86, 68, 94, 76, 97, 56, 98, 76, 87, 79, 90, 73, 93, 82, 69, 97, 98]
scores.sort()
max_score = scores[-1]
num = scores.count(max_score)
print("The max score is: {}".format(max_score))
print("{} student(s) got the max score".format(num))


# In[ ]:




