#!/usr/bin/env python
# coding: utf-8

# # Netflix Data Analysis

# In[6]:


import pandas as pd
data = pd.read_csv("C:\\Users\\biswa\\Downloads\\file.csv")


# In[7]:


data


# In[8]:


data.head()


# In[9]:


data.tail()


# In[11]:


data.shape


# In[12]:


data.size


# In[13]:


data.columns


# In[14]:


data.dtypes


# In[15]:


data.info()


# # Task 1 - Is there any Duplicate Record in the dataset ? If yes then remove the duplicate records

# In[16]:


data[data.duplicated()]


# In[17]:


data.drop_duplicates(inplace = True)


# In[18]:


data[data.duplicated()]


# In[19]:


data.shape


# # Task 2 - Is there any NULL value present in any column ? Show with Heat-Map

# In[20]:


data.isnull()


# In[21]:


data.isnull().sum()                                                        #to show count of null values in each column


# In[22]:


import seaborn as sns


# In[23]:


sns.heatmap(data.isnull())


# # Q1- For 'House of Cards' what is the show id and who is the director of the show?

# In[30]:


data[data['Title'].isin(['House of Cards'])]


# In[31]:


data[data['Title'].str.contains('House of Cards')]               #alternative for isin


# # Q2 - In which year highest number of TV shows and Movies were released ?Show with bar graph
# 

# In[42]:


data['Date_N'] = pd.to_datetime(data['Release_Date'])


# In[43]:


data.head()


# In[44]:


data.dtypes


# In[40]:


data['Date_N'].dt.year.value_counts()


# In[45]:


data['Date_N'].dt.year.value_counts().plot(kind = 'bar')


# # Q3 - How many TV shows and Movies are in the dataset ?Show with bar graph
# 

# In[48]:


data.groupby('Category').Category.count()                       #to group all unique items of a column and show their count 


# In[50]:


sns.countplot(data['Category'])


# # Q4 - Show all the movies that were released in the year 2000
# 

# In[51]:


data['Year'] = data['Date_N'].dt.year


# In[52]:


data.head(2)


# In[55]:


data[(data['Category'] == 'Movie') & (data['Year']==2000)]


# # Q5 - Show only the titles of all TV shows that were released in India only

# In[56]:


data[(data['Category'] == 'TV Show') & (data['Country']== 'India')]


# In[57]:


data[(data['Category'] == 'TV Show') & (data['Country']== 'India')]['Title']              #to show only the titles


# # Q6 - Show top 10 Directors who gave the the highest number of TV Shows and Movies to Netflix 

# In[58]:


data['Director'].value_counts().head(10)


# # Q7 - Show all the records where '' Category is Movie and Type is Comedies'' or "Country is United Kingdom"

# In[59]:


data[(data['Category'] == 'Movie') & (data['Type']== 'Comedies')]


# In[61]:


data[(data['Category'] == 'Movie') & (data['Type']== 'Comedies')| (data['Country'] == 'United Kingdom')]


# # Q8 - In how many movies/shows Tom Cruise was cast?

# In[65]:


data[data['Cast'] == ('Tom Cruise')]


# In[67]:


data[data['Cast'].str.contains('Tom Cruise')]                           #cannot work on null values


# In[68]:


data_new = data.dropna()
data_new.head(2)


# In[69]:


data_new[data_new['Cast'].str.contains('Tom Cruise')]


# # Q9 - What are the different Ratings defined by Netflix ?

# In[70]:


data['Rating'].nunique()


# In[71]:


data['Rating'].unique()


# # Q9.1 How many Movies got the 'TV-14' rating in Canada ?

# In[72]:


data[(data['Category'] == 'Movie') & (data['Rating']== 'TV-14')].shape


# In[73]:


data[(data['Category'] == 'Movie') & (data['Rating']== 'TV-14') & (data['Country']=='Canada')].shape


# # Q9.2 How many TV Shows got the 'R' rating , after year 2018 ?

# In[74]:


data[(data['Category'] == 'TV Show') & (data['Rating']== 'R')]


# In[76]:


data[(data['Category'] == 'TV Show') & (data['Rating']== 'R') & (data['Year'] > 2018)]


# # Q10 - What is the maximum duration of a Movie/Show on Netflix ?
# 
# 

# In[77]:


data['Duration'].unique()


# In[78]:


data.Duration.dtypes


# In[80]:


data[['Minutes','Unit']] = data['Duration'].str.split(' ' , expand=True)


# In[81]:


data.head(2)


# In[82]:


data['Minutes'].max()


# # Q11 - Which individual Country has the Highest number of TV Shows?

# In[83]:


data.head(2)


# In[84]:


data_tvshow = data[data['Category'] == 'TV Show']


# In[85]:


data_tvshow.head(2)


# In[86]:


data_tvshow.Country.value_counts()


# In[87]:


data_tvshow.Country.value_counts().head(1)


# # Q12 - How can we sort the dataset by year?

# In[88]:


data.head(2)


# In[89]:


data.sort_values(by='Year')


# In[90]:


data.sort_values(by='Year' , ascending = False)


# # Q13 - Find all the instances where :

# # Category is 'Movie' and Type is 'Dramas'

# # Or Category is 'TV Show' and Type is 'Kids TV'

# In[91]:


data.head(2)


# In[92]:


data[(data['Category'] == 'Movie') & (data['Type']== 'Dramas')]


# In[93]:


data[(data['Category'] == 'Movie') & (data['Type']== 'Dramas') | (data['Category'] == 'TV Show') & (data['Type']== 'Kids TV')]


# # End of Project

# In[ ]:




