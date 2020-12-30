import requests
import json 
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import splinter 
import selenium
import pandas as pd

mars_dict={}

def scrape_info():

    executable_path = {'executable_path' : 'chromedriver.exe'}
    browser = splinter.Browser('chrome', **executable_path, headless=False)

    # Title & paragraph
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    results=soup.find_all('div', class_="content_title")[1]
    news_title=results.find('a').text.strip()
    news_p = soup.find('div', class_='article_teaser_body').text.strip()
    mars_dict["news_title"]=news_title
    mars_dict["news_p"]=news_p

    # Featured img url
    space_url="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(space_url)
    browser.click_link_by_partial_text("FULL IMAGE")
    browser.click_link_by_partial_text("more info")
    html = browser.html
    soup = bs(html, 'html.parser')
    mars_img=soup.find("img", class_="main_image")["src"]
    split=space_url.split("/spaceimages/")[0]
    featured_image_url=split+mars_img
    mars_dict["featured_img_url"]= featured_image_url   

    # Mars Facts
    space_facts_url="https://space-facts.com/mars/"
    browser.visit(space_facts_url)
    html = browser.html
    mars_facts_tables=pd.read_html(space_facts_url)
    df_facts_table=mars_facts_tables[0]
    mars_html=df_facts_table.to_html()
    mars_html_table=mars_html.replace('\n', '')
    mars_dict["mars_html_table"]=mars_html_table

    # Mars Images
    hemisphere_url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemisphere_url) 
    html = browser.html
    soup = bs(html, 'html.parser')


    #loop through divs
    hemisphere_img_urls=[]
    items=soup.find_all('div', class_='item')

    for item in items:
        dict_s={}
        browser.visit(hemisphere_url) 
        title=item.find('h3').get_text()
        browser.click_link_by_partial_text(title)
        html = browser.html
        soup = bs(html, 'html.parser')
        img_url=soup.find("img", class_="wide-image")["src"]
    
        
        dict_s["title"] = title
        dict_s["img_url"]=img_url
                
        hemisphere_img_urls.append(dict_s)

    mars_dict["hemisphere_img_urls"]=hemisphere_img_urls


    return mars_dict
    
            







