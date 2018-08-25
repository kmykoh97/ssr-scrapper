# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 17:03:28 2018

@author: kmykoh97
"""



# import the library used to query a website
from urllib.request import urlopen
    
# import the Beautiful Soup to parse the contents obtained from website
from bs4 import BeautifulSoup



def getLink(url):
    # query the website and return the html contents
    htmlContent = urlopen(url)
    
    # parse the html and store it in Beautiful Soup format
    bs = BeautifulSoup(htmlContent, 'html.parser')
    
    # print(bs.prettify()) # print parsed html
    
    group = bs.find_all('pre', "prettyprint linenums") # get all elements with specific tag into a list
    contentString = group[len(group) - 1].string # get the last item then convert into string
    lines = contentString.splitlines() # split the multiline string into list of string with '\n' as separator
    result = lines[2] # get the 3rd line
    
    return result