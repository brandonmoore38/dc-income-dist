#!/usr/bin/env python
# coding: utf-8

# In[1]:


#/Users/brandonmoore/Downloads/Income by Ward.csv

import pandas as pd


# In[6]:


import pandas as pd
from pathlib import Path
import glob
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import numpy as np


# In[7]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[8]:


df=pd.read_csv('/Users/brandonmoore/Downloads/Income by Ward.csv')


# In[9]:


df.head()


# In[24]:





# In[17]:



df.rename(columns={'PctBlackNonHispBridge':'Percentage of Black Residents'})


# In[ ]:





# In[27]:


#/Users/brandonmoore/Downloads/Income by Ward copy.json

sns.barplot(x='Ward', y='AvgFamilyIncAdj', hue='timeframe', data=df);


# In[14]:


sns.barplot(x='Ward', y='Percentage of Black Residents, hue='timeframe', data=df);


# In[ ]:




