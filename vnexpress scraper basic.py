# -*- coding: utf-8 -*-
"""
Created on Tue May 12 00:56:04 2020

@author: PC
"""


from bs4 import BeautifulSoup
from urllib.error import URLError
from urllib.error import HTTPError
from urllib.request import urlopen
import time
def scraping_vnexpress():
    try:
        html = urlopen('https://vnexpress.net/').read()
    except URLError as e:
        print('URL Error!')
    except HTTPError as e:
        print(e)
    else:
        print('Succesfully read!')
    time.sleep(3)
    bsObject = BeautifulSoup(html, 'html.parser')
    tagname = ['h1','h2','h3','h4','h5']
    titles = []
    for tag in tagname:
        if tag != tagname[0]:
            titles += bsObject.find_all(tag, {'class':'title-news'})
        else:
            titles = bsObject.find_all(tag, {'class':'title-news'})
    n = 0
    for title in titles:
        print(title.text)
        n += 1
        print(n)
    
scraping_vnexpress()