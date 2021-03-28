#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd # Pandas
import numpy as np # Numpy
import matplotlib.pyplot as plt # Matplotlibrary
import seaborn as sns # Seaborn Library
get_ipython().run_line_magic('matplotlib', 'inline')


# In[13]:


# Load the Dataset in Python
tips = sns.load_dataset("tips")
tips.head()


# In[16]:


sns.distplot(tips["total_bill"], bins=16, color="blue")
# Binsize is calculated using square-root of row count.


# In[17]:


sns.jointplot(x = "total_bill", y = "tip", data = tips, color="blue")


# In[18]:


# Jointplot - Scatterplot and Histogram
sns.jointplot(x = "total_bill", y = "tip", data = tips, kind ="hex",
color="lightcoral")


# In[19]:


# kind : { "scatter" | "reg" | "resid" | "kde" | "hex" }


# In[20]:


# Jointplot - Scatterplot and Histogram
sns.jointplot(x = tips["total_bill"], y = tips["tip"],kind = "kde", 
color="purple") # contour plot


# In[21]:


# Pairplot of Tips
sns.pairplot(tips, hue = "sex", palette="Set2")
# this  will color the plot gender wise


# In[22]:


# Barplot
sns.barplot(x ="sex" , y ="total_bill" , data=tips)
# Inference - Total Bill Amount for males is more than Females.


# In[23]:


# Lets Plot Smoker Vs Total Bill :: The purpose is to find out if 
# Smokers pay more bill than Non Smokers
sns.barplot(x = "smoker", y = "total_bill", data =tips)
# Inference - More Bill for Smokers


# In[24]:


# LM PLot
sns.lmplot(x = "total_bill", y = "tip", data = tips, hue="day")


# In[ ]:




