#!/usr/bin/env python
# coding: utf-8

# In[42]:


import numpy as np
import pandas as pd
import statsmodels.stats.proportion as ssp


# In[43]:


data = pd.read_csv('/Users/zhoumin/Desktop/cookie_cats.csv')
data.head()


# In[44]:


data.info


# In[45]:


data.isnull().sum()


# In[46]:


data.duplicated().sum()


# In[47]:


print('版本值',data.version.unique())


# In[48]:


print('次日留存率',data.retention_1.unique())


# In[49]:


print('七日留存率',data.retention_7.unique())


# In[50]:


data.to_csv('data_cleaned.csv')


# In[51]:


retention=data.groupby('version').agg({'userid':'count','retention_1':sum,'retention_7':sum})
retention


# In[52]:


retention_rate=pd.DataFrame(index=['gate_30','gate_40'],columns=['次日留存率','七日留存率'])
for i in range(0,2):
    retention_rate.iloc[i,0]=retention.iloc[i,1] / retention.iloc[i,0]
    retention_rate.iloc[i,1]=retention.iloc[i,2] / retention.iloc[i,0]
retention_rate
# retention_rate = pd.DataFrame(index = ['gate_30','gate_40'],columns = ['次日留存率','七日留存率'])
# for i in range(0,2):
#     retention_rate.iloc[i,1] = retention.iloc[i,2] / retention.iloc[i,0]
#     retention_rate.iloc[i,0] = retention.iloc[i,1] / retention.iloc[i,0] 
# retention_rate


# In[69]:


z_score, p_value=ssp.proportions_ztest(count=retention.retention_1,nobs=
                                      retention.userid,alternative='smaller')
print("Z:",z_score)
print("P:",p_value)


# In[54]:


#此时次日留存率为0.96，大于0.05，所以无法拒绝原假设(H0)
#此时原假设是A比B好 H0：A与B没有显著性差异 H1:p(A)>= p(B)
#所以证明A与B没有显著性差异


# In[67]:


z_score, p_value=ssp.proportions_ztest(count=retention.retention_7, nobs=retention.userid,alternative='smaller')
print("Z:",z_score)
print("P:",p_value)

# z_score, p_value = ssp.proportions_ztest(count = retention.retention_7, nobs = retention.userid, alternative='smaller')
# print("Z值为：", z_score)
# print("P值为：", p_value)


# In[ ]:




