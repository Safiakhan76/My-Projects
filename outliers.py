#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[10]:


df=pd.read_csv(r"C:\Users\shaba\OneDrive\Desktop\machine learning\height.csv")


# In[11]:


df


# In[17]:


upper_limit=df['height'].mean()+2*df['height'].std()
upper_limit


# In[18]:


lower_limit=df['height'].mean()-2*df['height'].std()
lower_limit


# In[14]:


df2=df[(df.height>upper_limit)|(df.height<lower_limit)]


# In[15]:


df2


# In[16]:


df2.shape


# In[20]:


df2.describe()


# In[21]:


df3=df[(df.height<upper_limit)&(df.height>lower_limit)]


# In[22]:


df3


# In[23]:


df3.shape


# In[24]:


df3.describe()


# In[26]:


fd=pd.read_csv(r"C:\Users\shaba\OneDrive\Desktop\machine learning\diabetes.csv")


# In[27]:


fd


# In[28]:


upper_limit=fd['Pregnancies'].mean()+2*fd['Pregnancies'].std()


# In[29]:


lower_limit=fd['Pregnancies'].mean()-2*fd['Pregnancies'].std()


# In[30]:


fd1=fd[(fd.Pregnancies>upper_limit)|(fd.Pregnancies<lower_limit)]


# In[31]:


fd1


# In[32]:


fd2=fd[(fd.Pregnancies<upper_limit)&(fd.Pregnancies>lower_limit)]


# In[33]:


fd2


# In[34]:


inter_quartile_range=df.height.quantile(0.75)-df.height.quantile(0.25)


# In[37]:


lower_limit2=df.height.quantile(0.5)-(1.5*inter_quartile_range)
upper_limit2=df.height.quantile(0.75)+(1.5*inter_quartile_range)


# In[38]:


df4=df[(df.height<upper_limit2)&(df.height>lower_limit2)]


# In[39]:


df4


# In[40]:


df5=df[(df.height>upper_limit2)|(df.height<lower_limit2)]


# In[41]:


df5


# In[ ]:




