#!/usr/bin/env python
# coding: utf-8

#    # EDA on Sales Export 2019-2020

# ### 1. Importing Pandas and Numpy for Implimenting EDA

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# ### 2. Dataset Loading Procedures 

# In[2]:


Sales_Export = pd.read_csv(r"C:\Users\sande\OneDrive\Desktop\Datasets\sales dataset 2023\Sales-Export_2019-2020(new).csv")


# In[3]:


Sales_Export


# In[5]:


Sales_Export.head(10)              # Showing first 10 Rows


# ### 2.1 Understanding the Dataset

# In[52]:


Sales_Export.shape               # There are 1000 number of Rows and 10 Columns Present in the Dataset


# In[82]:


Sales_Export.columns


# In[4]:


Sales_Export['date'] = pd.to_datetime(Sales_Export['date'])


# In[5]:


Sales_Export['day'] = Sales_Export['date'].dt.day
Sales_Export['month'] = Sales_Export['date'].dt.month
Sales_Export['year'] = Sales_Export['date'].dt.year


# In[6]:


Sales_Export


# In[7]:


Sales_Export.drop('day', inplace=True, axis=1)


# In[8]:


Sales_Export


# In[9]:


import calendar


# In[10]:


Sales_Export['month'] = Sales_Export['month'].apply(lambda x: calendar.month_abbr[x])


# In[11]:


Sales_Export


# In[21]:


Sales_Export.describe()


# In[22]:


Sales_Export.info()


# In[23]:


Sales_Export.isnull().sum()


# In[24]:


Sales_Export.dtypes


# ## 3. Possible Insights that Can be Extracted From Dataset

# ### 3.1 Number of Countries are paid for Beauty Category.

# In[25]:


Sales_Export[['country','category']]


# In[26]:


group = Sales_Export.groupby('category')['country']


# In[27]:


group.head(2)


# In[28]:


country_group = group.count().head(10)


# In[29]:


country_group


# In[146]:


x_axis = Sales_Export[['country']]


# In[147]:


style.use('ggplot')

plt.figure(figsize = (25,7))

plt.hist(x_axis,bins = 50,histtype='stepfilled',align='mid',orientation='vertical' , color = '#4863A0' ,label='Histogram',stacked=False )
plt.xlabel('country')
plt.ylabel('Count of Sells')
plt.title('Sells Country wise')
plt.legend()
plt.show()


# In[142]:


y_axis = Sales_Export[['category']]


# In[148]:


plt.figure(figsize = (25,7))
plt.hist(y_axis,bins = 50,histtype='stepfilled',align='mid', color = '#3090C7',orientation='vertical' ,label='Histogram',stacked=False )
plt.xlabel('category')
plt.ylabel('category_count')
plt.title('Sells of Categories')
plt.legend()
plt.show()


# In[98]:


Country_catagories = Sales_Export[Sales_Export['category'] == 'Beauty'].count().head(1)


# In[31]:


Country_catagories 


# ### 3.2  The Best known Sales manager in the sales field.

# In[32]:


Sales_Export.head(5)


# In[33]:


Sales_Export[['category','sales_manager']].head(5)


# In[19]:


best_manager = Sales_Export.groupby('sales_manager')['category']


# In[44]:


List_maneger = Sales_Export[['sales_manager']]


# In[45]:


List_maneger


# In[35]:


best_manager.count().head(5)


# In[36]:


best_manager.count().sort_values(ascending = False).head(1)


# In[150]:


y_axis = best_manager.count().head(5)


# In[151]:


x_axis = List_maneger


# In[152]:


style.use('ggplot')

plt.figure(figsize = (25,7))
plt.hist(x_axis,bins = 50,histtype='stepfilled',align='mid',orientation='vertical',color='#0504aa',label='Histogram',stacked=False)
plt.xlabel('sales_manager')
plt.ylabel('category')
plt.title('Best Sells by Manager')
plt.legend()
plt.show()


# ### 3.3 The order_id creates a highest cost in the saling market.

# In[37]:


Sales_Export.head(5)


# In[38]:


Sales_Export[['order_id' , 'cost']]


# In[39]:


Max_cost = Sales_Export['cost'].max()


# In[40]:


Max_cost


# In[41]:


Max_values = Sales_Export.max()


# In[42]:


Max_values


# In[43]:


Max_values[['order_id' , 'cost']]


# ### 3.4 The Most Tablet Selling Country.

# In[44]:


Sales_Export[['country' , 'device_type']]


# In[45]:


Tablet_Selling = Sales_Export.groupby('country')['device_type']


# In[46]:


Tablet_Selling.head(5)


# In[47]:


Tablet_Selling.count().sort_values(ascending = False).head(1)


# ### 3.5   Category of Products Sold by 'Jessamine Apank'

# In[48]:


Sales_Export[['category' , 'sales_manager']]


# In[49]:


Sold_Categories = Sales_Export[Sales_Export['sales_manager'] == 'Jessamine Apark'].head(5)


# In[50]:


Sold_Categories


# In[51]:


Sold_Categories[['sales_manager' , 'category']]


# ### 3.6 Number of Counties has sold PC Devices Coming Under Appliances Category

# In[52]:


Sales_Export[['country' , 'category' , 'device_type']]


# In[53]:


Appliances_Category = Sales_Export[Sales_Export['device_type'] == 'PC'].head()


# In[54]:


Appliances_Category.head()


# In[55]:


Appliances = Appliances_Category[['device_type' , 'category' , 'country']]


# In[56]:


Appliances


# In[57]:


Appliances_category = Appliances.groupby('country')['device_type']


# In[58]:


Appliances_category.count().head()  


# #### There is not a single country which sold PC in Appliances Category

# ### 3.7 The Average Cost spend by the Report from the year 2019-2020

# In[90]:


mean = Sales_Export[['cost', 'order_value_EUR']].mean().head()


# In[91]:


mean


# In[89]:


sns.lineplot(data = Sales_Export, x = 'cost' , y = 'order_value_EUR' , color='#0504aa' )
plt.title("Cost with Respect to Order_value_EUR")


# ### 3.8 Maximum Selling Month wise

# In[60]:


month_group = Sales_Export.groupby('month')['order_id']


# In[63]:


monthly_selling = month_group.count().sort_values(ascending = False ).head(12)


# In[64]:


monthly_selling


# In[84]:


x_axis = Sales_Export[['month']].sort_values(by = 'month' , ascending = False)


# *** Graph Between Categoral Count With Respect to Month

# In[85]:


style.use('ggplot')

plt.figure(figsize = (12,5))
plt.hist(x_axis,bins = 25,rwidth=0.55,align='mid',alpha=0.7, histtype='bar',orientation='vertical', edgecolor='black',color='#0504aa',label='Histogram',stacked=False)
plt.xlabel('month')
plt.grid(axis='y', alpha=0.75)
plt.ylabel('Total no of Sells')
plt.title('Monthly Orders Histogram')
max_numbers = y_axis.max()
plt.legend()
plt.show()


# ### 4.1 Correlation

# In[12]:


Sales_Export.corr()


# ### 4.2 Co-varience

# In[134]:


Sales_Export.cov()


# ### 5.0 Heatmap

# In[133]:


sns.set()
plt.subplots(figsize = (5,5))
sns.heatmap(Sales_Export.corr(),annot = True)

