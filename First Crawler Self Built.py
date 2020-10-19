# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 13:48:53 2020

@author: PC
"""
import re
from urllib.parse import urlparse
import requests
from Links import *
import csv


main_lk = L_1
print(main_lk)
bucket = []

class Crawler():
    def __init__(self, inilink, stop):
        self.inilink = inilink
        self.checkpoint = set()
        self.stop = stop
        self.count = 0
    
    def html(self,url):
        try:
            html = requests.get(url)
        except Exception as e:
            print(e)
            return ""
        return html.text
    
    def get_link(self,url):
        html = self.html(url)
        r_parse = urlparse(url)
        base_lk = r_parse.scheme +'://'+r_parse.netloc
        links = list(set(re.findall('href="([-+./:\w]+)"', html)))
        
        for x in range(len(links)):
            parse = urlparse(links[x])
            if not parse.netloc:
                new_lk = base_lk + links[x]
                links[x] = new_lk
        return links 
    
#    def get_info(self,url):
#        html = html(url)
#        bucket.append()
        
    def csv(self,url):
        print(url)
        with open('links.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([url])
            
            
    def crawl(self, url):
        l_lk = self.get_link(url)
        for link in l_lk:
            self.count = self.count + 1
            if link in self.checkpoint:
                continue
            if self.count < self.stop:
                self.csv(link)
                #print(link)
                self.checkpoint.add(link)
                self.crawl(link)
                
            else:
                continue

    
    def start(self):
        self.crawl(self.inilink)
    
if __name__== "__main__":
    crawler = Crawler(main_lk,10000)
    crawler.start()
    
    
    
    
    
    
    
    
    
    