#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


import requests
import json 
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import splinter 
import selenium
import pandas as pd


# In[2]:

def scrape_info():
    executable_path = {'executable_path' : 'chromedriver.exe'}
    browser = splinter.Browser('chrome', **executable_path, headless=False)

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html


# In[3]:


    soup = bs(html, 'html.parser')
    #print(soup.prettify())


    # In[4]:


    results=soup.find_all('div', class_="content_title")[1]
    results


    # In[5]:

    # In[6]:


    news_title=results.find('a').text.strip()
    news_title


    # In[7]:


    news_p = soup.find('div', class_='article_teaser_body').text.strip()
    news_p


    # In[8]:


    space_url="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"


    # In[9]:


    browser.visit(space_url)
    html = browser.html


    # In[10]:


    soup = bs(html, 'html.parser')
    #print(soup.prettify())


    # In[11]:


    image_url=soup.find("article")['style']
    image_url


    # In[12]:


    s=image_url.split("'")[1]
    s


    # In[13]:


    featured_image_url=space_url+s
    featured_image_url


    # In[14]:


    browser.click_link_by_id("full_image")


    # In[15]:


    space_facts_url="https://space-facts.com/mars/"


    # In[16]:


    browser.visit(space_facts_url)
    html = browser.html


    # In[17]:


    soup = bs(html, 'html.parser')
    #print(soup.prettify())


    # In[18]:


    table=soup.find("table", class_="tablepress")
    table


    # In[19]:


    hemisphere_url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"


    # In[20]:


    browser.visit(hemisphere_url)
    html = browser.html


    # In[21]:


    soup = bs(html, 'html.parser')
    #print(soup.prettify())


    # In[22]:


    browser.click_link_by_partial_text("Cerberus Hemisphere Enhanced")


    # In[23]:


    title_1=browser.find_by_tag("h2").text
    title_1


    # In[24]:


    browser.click_link_by_text("Sample")


    # In[25]:


    img1_url=browser.url


    # In[26]:


    browser.visit(hemisphere_url)


    # In[27]:


    browser.click_link_by_partial_text("Schiaparelli Hemisphere Enhanced")


    # In[28]:


    title_2=browser.find_by_tag("h2").text
    title_2


    # In[29]:


    browser.click_link_by_text("Sample")


    # In[30]:


    img2_url=browser.url


    # In[31]:


    img2_url


    # In[32]:


    browser.visit(hemisphere_url)


    # In[33]:


    browser.click_link_by_partial_text("Syrtis Major Hemisphere Enhanced")


    # In[34]:


    title_3=browser.find_by_tag("h2").text
    title_3


    # In[35]:


    browser.click_link_by_text("Sample")
    img3_url=browser.url


    # In[36]:


    img3_url


    # In[37]:


    browser.visit(hemisphere_url)


    # In[38]:


    browser.click_link_by_partial_text("Valles Marineris Hemisphere Enhanced")


    # In[39]:


    title_4=browser.find_by_tag("h2").text
    title_4


    # In[40]:


    browser.click_link_by_text("Sample")
    img4_url=browser.url


    # In[41]:


    browser.visit(hemisphere_url)


    # In[44]:


    otherData={}


    # In[52]:


    otherData["Nasa news title"] = news_title
    otherData["Nasa news paragraph"]=news_p
    otherData["Featured Image"]=featured_image_url


    # In[59]:


    otherData["Facts Table"]=table
    otherData


    # In[46]:


    hemisphere_image_urls = {}


    # In[56]:


    hemisphere_image_urls[title_1]=img1_url
    hemisphere_image_urls[title_2]=img2_url
    hemisphere_image_urls[title_3]=img3_url
    hemisphere_image_urls[title_4]=img4_url


    # In[ ]:

    final_dict={}
    final_dict["Dict 1"]= otherData
    final_dict["Dict 2"]=hemisphere_image_urls


    return final_dict


    # In[ ]:





# %%
