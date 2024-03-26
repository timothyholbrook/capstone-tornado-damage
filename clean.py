#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pandas')


# In[2]:


import pandas as pd

#Read data files
df = pd.read_csv('data/1950-23 damage_fatal_injury.csv')
df1 = pd.read_csv('data/1950-2023_tor_fatalities.csv')



# In[3]:


df


# In[4]:


df1


# In[5]:


#Sort the DataFrame by the year column in descending order
df1 = df1.sort_values(by='Date', ascending=False)

#Reset the index
df1.reset_index(drop=True, inplace=True)

#Drop the first row
df = df.drop(0)

#Remove commas from values
df['Direct Injury'] = df['Direct Injury'].str.replace(',', '')
df['Direct Fatality'] = df['Direct Fatality'].str.replace(',', '')
df['Property Damage'] = df['Property Damage'].str.replace(',', '')
df['Crop Damage'] = df['Crop Damage'].str.replace(',', '')

#Convert Data Types
df['Direct Injury'] = df['Direct Injury'].astype(int)
df['Indirect Injury'] = df['Indirect Injury'].astype(int)
df['Direct Fatality'] = df['Direct Fatality'].astype(int)
df['Indirect Fatality'] = df['Indirect Fatality'].astype(int)

#Check Data Types
print(df.dtypes)
print(df1.dtypes)


# In[6]:


#Remove the last two characters
df1['Date'] = df1['Date'].astype(str).str[:-2]

#Rename Date column from df1
df1 = df1.rename(columns={'Date': 'Year'})

#Save to csv
df1.to_csv('modified_date.csv', index=False)


# In[7]:


#Combine columns
df['Injuries'] = df['Direct Injury'] + df['Indirect Injury']
df['Fatalities'] = df['Direct Fatality'] + df['Indirect Fatality']


# In[8]:


#Save as new csv
df.to_csv('combined_file.csv', index=False)
df2 = pd.read_csv('combined_file.csv')


# In[9]:


#Display df
df


# In[10]:


#Display df1
df1


# In[11]:


#Display df2
df2


# In[ ]:




