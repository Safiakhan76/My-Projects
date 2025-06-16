#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score 
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()


# In[2]:


df=pd.read_csv(r"C:\Users\shaba\OneDrive\Desktop\machine learning\diabetes.csv")
df


# In[25]:


x=df.values[:,1:9]
y=df.values[:,9]
y


# In[31]:


X_train,X_test,y_train,y_test= train_test_split( x, y, test_size = 0.3, random_state = 1000)


# In[32]:


clf_entropy = tree.DecisionTreeClassifier(criterion = "entropy", max_depth=3, min_samples_leaf=500)


# In[33]:


clf_entropy.fit(X_train, y_train)


# In[34]:


clf_entropy = DecisionTreeClassifier(criterion = "entropy", random_state = 1000,max_depth=3, min_samples_leaf=50)
clf_entropy.fit(X_train, y_train)
y_pred = clf_entropy.predict(X_test)
y_pred


# In[35]:


print("Accuracy is ", accuracy_score(y_test,y_pred)*100)


# In[ ]:





# In[ ]:




