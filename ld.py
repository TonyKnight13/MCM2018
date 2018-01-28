
# coding: utf-8

# In[99]:


import pandas as pd
import numpy as np


df = pd.read_csv('a4.csv',encoding='GBK')
print(df)


# In[127]:


def func(x):
    if type(x['MARRY_STATUS']) == str:
        return True
    return False
    return np.isnan(x['MARRY_STATUS'])

df[df.apply(func, axis=1)]


# In[57]:



