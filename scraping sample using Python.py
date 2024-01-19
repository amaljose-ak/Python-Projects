#!/usr/bin/env python
# coding: utf-8

# In[30]:


from bs4 import BeautifulSoup
import requests


# In[31]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')


# In[34]:


soup.find('table')


# In[35]:


soup.find_all('table')[1]


# In[36]:


soup.find('table', class_ = 'wikitable sortable')


# In[40]:


table = soup.find_all('table')[1]


# In[41]:


world_titles = table.find_all('th')


# In[42]:


world_table_titles = [title.text.strip() for title in world_titles]

print(world_table_titles)


# In[ ]:




