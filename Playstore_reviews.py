#!/usr/bin/env python
# coding: utf-8

# # HiCounselor Company

# # Playstore Apps analysis & visualization

# ## Team Name: Girls Squad
# ### Team Members: Smriti Kumari, Ramya Rao Thella, Raga Rasagna Paruchuri, Punam Nagrale

# # Task 1: Pre-processing the data

# ## Subtask 1: Removing duplicate rows

# ### Importing Libraries

# In[1]:


import numpy as np
import pandas as pd


# ### Importing the playstore_reviews dataset

# In[2]:


file = pd.read_csv('playstore_reviews.csv', index_col='App')
file.head()


# ### Printing the information about dataset

# In[3]:


file.info()


# ### Subtask1: Removing duplicate data

# In[4]:


file.drop_duplicates(keep='first', inplace=False)


# ### Printing the information after removing the duplicates from the dataset

# In[5]:


file.info()


# ## Subtask2: Remove irrelevant values from each column (if any)
# 

# ### Unique values for Translated_Review Column

# In[6]:


print(file['Translated_Review'].unique())


# In[7]:


file = file.dropna(subset=['Translated_Review'])


# In[8]:


file.info()


# In[9]:


print(file['Translated_Review'].unique())


# ### Unique values for Sentiment Column 

# In[10]:


print(file['Sentiment'].unique())


# ### Unique values for Sentiment Polarity Column

# In[11]:


for each_sentiment_polarity in file['Sentiment_Polarity'].unique():
    print(each_sentiment_polarity)


# ### Unique values for Sentiment Subjectivity Column

# In[12]:


for each_sentiment_subjectivity in file['Sentiment_Subjectivity'].unique():
    print(each_sentiment_subjectivity)


# ## Subtask 3: Exporting the cleaned dataset as a .csv file 

# In[13]:


file.to_csv("Playstore_reviews_cleaned_file.csv")

