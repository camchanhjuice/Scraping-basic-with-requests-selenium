# -*- coding: utf-8 -*-
"""
Created on Mon May 18 15:50:42 2020

@author: PC
"""

# import libraries
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
# specify the url
urlpage = 'https://groceries.asda.com/search/yoghurt' 

urlpage2= 'https://finance.vietstock.vn/AFC/thong-ke-giao-dich.htm?grid=market'
print(urlpage2)
# run firefox webdriver from executable path of your choice
chrome_path = r"C:\Users\PC\Desktop\chromedriver.exe"
driver = webdriver.Chrome(executable_path = chrome_path)
# get web page
driver.get(urlpage2)
# execute script to scroll down the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# sleep for 30s
time.sleep(15)
# driver.quit()
# find elements by xpath
# at time of publication, Nov 2018:
# results = driver.find_elements_by_xpath("//*[@id='componentsContainer']//*[contains(@id,'listingsContainer')]//*[@class='product active']//*[@class='title productTitle']")
# updated Nov 2019:
'''results = driver.find_elements_by_xpath("""//*[@id="stock-trading-result"]/table/tbody""")
for x in results:
    print(x)'''


results = driver.find_elements_by_xpath("//*[@class=' co-product-list__main-cntr']//*[@class=' co-item ']//*[@class='co-product']//*[@class='co-item__title-container']//*[@class='co-product__title']")

results2 = driver.find_elements_by_xpath("//*/td[contains(@class,'text-right')]")
#("//*[@class='table-responsive stock-trading-result']//*[@class='table table-striped table-hover table-bordered m-b-xs']/tbody/tr/td[contains(@class,'text-right')]")
#//*/tbody/tr/td[contains(@class,'text-right')]
print('Number of results', len(results2))
for num,ele in enumerate(results2):
    print(num,ele.text)