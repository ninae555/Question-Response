#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install altair


# In[1]:


import pandas as pd
import numpy as np
import matplotlib as plt
import altair as alt


# In[2]:


df = pd.read_csv('/Users/admin/Downloads/Data Science Sample Data - Sheet1.csv')


# In[3]:


print(df.head())
print(df.describe())
print(df.info())


# In[4]:


# we can see that there is a missing value for checkinDatTime column
print(df['Check in DateTime'])

df['Check in DateTime'].fillna('1/6/2023 4:00 PM', inplace=True)


# In[5]:


# 11th value is incorrect in this column

df['Check in DateTime'].iloc[11] = '1/15/2023 4:00 PM'
print(df['Check in DateTime'])

print(df['Check in Note'])
df['Check in Note'].fillna('No Notes made on this day',inplace=True)


# In[11]:


a = alt.Chart(df).mark_line().encode(
    x = alt.X('Check in DateTime', type='temporal'),
    y = alt.Y('Check in %', type='quantitative'),
    tooltip = ['Intention (Boolean):O','Check in Note:O']
).properties(title = "Goal Accomplishment")
a


# In[10]:


df.plot(y = "Check in %", x = 'Check in DateTime')

