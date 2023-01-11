#!/usr/bin/env python
# coding: utf-8

# In[1]:


# # HiCounselor Company

# # Playstore Apps analysis & visualization

# ## Team Name: Girls Squad
# ### Team Members: Smriti Kumari, Ramya Rao Thella, Raga Rasagna Paruchuri, Punam Nagrale



# In[ ]:


# # Task 1: Pre-processing the data

# ## Subtask 1: Removing duplicate rows

# ### Importing Libraries


# In[2]:


import pandas as pd
import numpy as np
from numpy import nan


# In[3]:


# ### Importing the playstore_reviews dataset

file=pd.read_csv("F:/MS-UTD/datasets/playstore_apps.csv", index_col="App")
file.head()


# In[4]:


# ### Subtask1: Removing duplicate data
file.drop_duplicates(keep='first',inplace=True)


# In[5]:


# ### Printing the information about dataset
file.info()


# In[6]:


# ## Subtask2: Remove irrelevant values from each column (if any)
# 
# ### Unique values for Category Column
print(file['Category'].unique())


# In[7]:


print(file[file['Category']=='1.9'])


# In[10]:


file.drop("Life Made WI-Fi Touchscreen Photo Frame",inplace=True)


# In[11]:


print(file['Category'].unique())


# In[12]:


# ### Unique values for Rating Column
print(file['Rating'].unique())


# In[13]:


# ### Unique values for Reviews Column
print(file['Reviews'].unique())


# In[17]:


# ### Unique values for Size Column
print(file['Size'].unique())


# In[14]:


print(file[file['Size']=='Varies with device'])


# In[15]:


# ### Unique values for Installs Column
print(file['Installs'].unique())


# In[16]:


# ### Unique values for Type Column
print(file['Type'].unique())


# In[17]:


print(file[file['Type']== nan])


# In[19]:


file.drop("Command & Conquer: Rivals",inplace=True)


# In[21]:


# ### Unique values for Type Column #checking
print(file['Type'].unique())


# In[22]:


# ### Unique values for Price Column
print(file['Price'].unique())


# In[23]:


# ### Unique values for Content Rating Column
print(file['Content Rating'].unique())


# In[24]:


print(file[file['Content Rating']== 'Unrated'])


# In[25]:


# ### Unique values for Genres Column
print(file['Genres'].unique())


# In[26]:


### Unique values for Last Updated Column
print(file['Last Updated'].unique())


# In[27]:


### Unique values for Current Version Column
print(file['Current Ver'].unique())


# In[28]:


### Unique values for Android Version Column
print(file['Android Ver'].unique())


# In[29]:


file.to_csv("F:/MS-UTD/datasets/cleaned_file_apps_final.csv")


# In[ ]:




