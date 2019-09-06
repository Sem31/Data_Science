#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import numpy as np

df = pd.read_csv('example')
print(df)


# In[8]:


pd.read_excel('Excel_Sample.xlsx',sheet_name = "Sheet1",index= False)


# In[10]:


from sqlalchemy import create_engine


# In[11]:


engine = create_engine("sqlite:///:memory:")


# In[15]:


df.to_sql('my_table',engine)


# In[16]:


sql_df = pd.read_sql('my_table',con = engine)


# In[17]:


sql_df


# In[ ]:




