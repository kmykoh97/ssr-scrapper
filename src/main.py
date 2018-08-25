# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 17:13:10 2018

@author: kmykoh97
"""



def main():
    ssrLink = getLink(url)
    information = decoder(ssrLink)
    
    print(information)



if __name__ == "__main__":
    from scrapper import getLink
    from ssrDecoder import decoder
    
    # specify the url
    url = "https://fangeqiang.com/408.html"
    
    main()