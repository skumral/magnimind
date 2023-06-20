#!/usr/bin/env python
# coding: utf-8

# ### Introduction
# 
# The objective of this project is to examine the effects of user engagement after seeing Ad A or Ad B
# 
#  
# 
# ### Problem
# An advertising company has developed a new ad to have users engage with their questionnaire. The company has shown the new ad to some users and a dummy ad to others and wants their data analyst team to interpret the results. Does the new ad generate more responses to their questionnaire? Is it statistically significant? Is the company justified in using the new ad? 
# 
#  
# 
# A/B testing is common in the business world and is a way to compare two versions of something to figure out which performs better. Figuring out which ad users prefer is a real life business problem that would be expected to know how to solve as a business data analyst. 
# 
# ### Data Science Approach
# 
# ·         Data wrangling/ data cleaning
# 
# ·         EDA - exploring the data
# 
# ·         Modeling - A/B testing
# 
# ·         Interpretation

# In[108]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ### Data Understanding

# In[109]:


df = pd.read_csv('AdSmartABdata - AdSmartABdata.csv')
df.head()


# In[110]:


# check if any null values
df.isnull().sum()


# In[111]:


# check if any duplicated values
df.duplicated().sum()


# In[112]:


df.info()


# In[113]:


df.describe()


# In[114]:


# list the unique values in each column
for col in df.columns:
    print(col, len(df[col].unique()), df[col].unique())


# In[115]:


# drop the rows with yes=0 and no=0 - no response
df = df.drop(df[(df['yes'] == 0) & (df['no'] == 0)].index)


# In[116]:


df


# ### Extract The Numbers We Need For The AB Testing

# In[117]:


exposed_yes = df[(df['experiment'] == 'exposed') & (df['yes'] == 1)]['yes'].sum()
exposed_yes


# In[118]:


exposed_no = df[(df['experiment'] == 'exposed') & (df['no'] == 1)]['no'].sum()
exposed_no


# In[119]:


control_yes = df[(df['experiment'] == 'control') & (df['yes'] == 1)]['yes'].sum()
control_yes


# In[120]:


control_no = df[(df['experiment'] == 'control') & (df['no'] == 1)]['no'].sum()
control_no


# In[121]:


data = {
    'control': [control_no, control_yes],
    'exposed': [exposed_no, exposed_yes]
}


# In[122]:


df2 = pd.DataFrame(data)
print(df2)


# ### A/B Testing

# #### Null and Alternative Hypotheses (Z-test for comparing proportions (2-sided))
# $$
#   \begin{cases}
#     H_0:& p_{con}=p_{exp}\\
#     H_1: &p_{con}\neq p_{exp}
# \end{cases}
# $$

# In[123]:


import numpy as np
from scipy.stats import norm


# In[124]:


X_con = control_yes              #clicks control
N_con = control_no + control_yes #impressions control
X_exp = exposed_yes              #clicks experimental
N_exp = exposed_no + exposed_yes #impressions experimental


# In[125]:


# Significance Level - called type I error - probability of rejecting the true null hypothesis
alpha = 0.05        


# In[126]:


# estimates of p_con and p_exp
p_con_hat = X_con / N_con
p_exp_hat = X_exp / N_exp # (who clicked yes when they saw the new ad) / (who saw the new ad)


# In[127]:


# estimate for the pooled probability of success
p_pooled_hat = (X_con + X_exp)/(N_con + N_exp)

# estimate for pooled variance
pooled_variance = p_pooled_hat*(1-p_pooled_hat) * (1/N_con + 1/N_exp)
#to calculate the standard error
#to see how far the difference of proportions from the mean of the standard distribution

# standard error
SE = np.sqrt(pooled_variance)


# In[128]:


# test statistics - standardized difference between two proportions
Test_stat = (p_exp_hat - p_con_hat)/SE


# In[129]:


# two sided test and using symmetry property of Normal distibution so we multiple with 2
p_value = norm.sf(Test_stat)*2


# In[130]:


# critical value usig the standard normal distribution
Z_crit = norm.ppf(1-alpha/2)


# In[131]:


# margin of error
m = SE * Z_crit


# In[132]:


# confidence interval
CI = [(p_exp_hat - p_con_hat) - SE * Z_crit, (p_exp_hat - p_con_hat) + SE * Z_crit]


# In[133]:


if np.abs(Test_stat) >= Z_crit:
    print("reject the null")
    print(p_value)
else:
    print("fail to reject the null")
    print(p_value)

    
# we can also do the same comparison between p and alpha
# p<alpha-> reject the null
# p>alpha-> fail to reject the null


# In[134]:


print("Test Statistics stat: ", Test_stat)
print("Z-critical: ", Z_crit)
print("P_value: ", p_value)
print("%95 Confidence Interval of 2 sample Z-test for proportions: ", np.round(CI,2)) 
#if the null value is in the CI, then you fail to reject the null hypothesis
 


# In[135]:


import matplotlib.pyplot as plt
z = np.arange(-3,3,  0.1)
plt.plot(z, norm.pdf(z), label = 'Standard Normal Distribution',color = 'purple',linewidth = 2.5)
plt.plot(Test_stat, 0, '*', color = 'red',linewidth = 2.5)
plt.fill_between(z[z>Z_crit], norm.pdf(z[z>Z_crit]), label = 'Right Rejection Region',color ='y' )
plt.fill_between(z[z<(-1)*Z_crit], norm.pdf(z[z<(-1)*Z_crit]), label = 'Left Rejection Region',color ='y' )
plt.title("Two Sample Z-test rejection region")
plt.legend(loc=(0,1))
plt.show()


# In[ ]:




