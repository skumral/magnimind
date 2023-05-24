#!/usr/bin/env python
# coding: utf-8

# 1- How many rows of data are in the DataFrame?
# 

# In[3]:


import pandas as pd
df = pd.read_csv("ksprojects.csv")
df.info()
# after running .info(), it is seen that there are 65418 rows. 


# 2- What are the names and data types of the columns?
# 

# In[10]:


column_names = df.columns
print(column_names)

column_types = df.dtypes
print(column_types)


# 3- Do any of the columns contain null values?
# 

# In[13]:


df.isnull().any()
#after running this, it is seen that column "usd_pledged" contains null values.


# In[21]:


df


# 4- Find all successful documentary projects and sort them by the amount pledged. Print the top 10 highest pledges.
# 

# In[24]:


df_succ = df[(df['category'] == 'Documentary') & (df['state'] == 'successful')]
df_sorted = df_succ.sort_values('usd_pledged', ascending=False)
df_sorted.head(10)


# 5- Create a new column named average_per_backer and set its value to the total amount pledged / number of backers.

# In[26]:


df['average_per_backer'] = df['usd_pledged'] / df['backers']
df


# 6- What happened to the rows with 0 backers? How can this be dealt with?
# 

# In[27]:


#I got NaN for those rows.


# 7- Drop all rows with 0 backers then repeat the previous exercise.
# 

# In[29]:


df = df.drop(df[df['backers']==0].index)
df['average_per_backer'] = df['usd_pledged'] / df['backers']
df


# 8- Create a DataFrame whose index is the first 10 letters of the alphabet and contains two more columns with first 10 prime numbers and the first 10 fibonacci numbers.
# 

# In[32]:


import math
def is_prime(number):
    if number < 2:
        return False
    for x in range(2, int(math.sqrt(number)) + 1):
        if number % x == 0:
            return False
    return True


def create_fibo(n):
    fibo = [0,1]
    for i in range(2, n):
        fibo.append(fibo[i-1]+fibo[i-2])
    return fibo[:n]

prime_num = [num for num in range(1,100) if is_prime(num)] [:10]
fibo_num = create_fibo(10)

df = pd.DataFrame({'Prime Numbers': prime_num,
                   'Fibonacci Numbers': fibo_num},
                 index=list('abcdefghij'))
df


# 9- Merge these two DataFrames into a single DataFrame: nycflights13.
# Please use the following dataset for merging purposes:
# https://tf-assets-prod.s3.amazonaws.com/tf-curric/data-science/flights.csv
# 
# https://tf-assets-prod.s3.amazonaws.com/tf-curric/data-science/airlines.csv
# 
# flights = pd.read_csv('https://tf-assets-prod.s3.amazonaws.com/tf-curric/data-science/flights.csv')
# airline = pd.read_csv('https://tf-assets-prod.s3.amazonaws.com/tf-curric/data-science/airlines.csv')
# 

# In[35]:


flights = pd.read_csv('https://tf-assets-prod.s3.amazonaws.com/tf-curric/data-science/flights.csv') 
airline = pd.read_csv('https://tf-assets-prod.s3.amazonaws.com/tf-curric/data-science/airlines.csv')
merge = pd.merge(flights, airline, on = 'carrier')
merge


# 10- Are there any missing values in this DataFrame? If so, drop them.
# 

# In[45]:


merge.isnull().any() #yes, there are missing values
dropped_df = merge.dropna()
dropped_df.isnull().any()


# 11- Merge these two DataFrames into a single DataFrame called census.
# Please use the following dataset for merging purposes:
# 
# 'https://tf-assets-prod.s3.amazonaws.com/tf-curric/data-science/state-populations.csv'
# 
# 'https://tf-assets-prod.s3.amazonaws.com/tf-curric/data-science/census-divisions.csv'
# 
# 

# In[46]:


#The links do not work, so I couldn't solve questions #11,12,13,14


# 12- Re-shape census so that one column contains all population measures, and another the year attributes.

# 13- Group the data by year and summarize it.
# 

# 14- Group the data by region, division and year and summarize it.
# 

# 15- Create a crosstab between state and category showing amount pledged as the value.
# Please refer to the following link for this practice:
# 
# https://tf-assets-prod.s3.amazonaws.com/tf-curric/data-science/ksprojects.csv
# 
# 

# In[51]:


df = pd.read_csv("ksprojects.csv")
cross_tab = pd.crosstab(df['state'], df['category'], values=df['usd_pledged'], aggfunc=sum)
cross_tab


# In[ ]:




