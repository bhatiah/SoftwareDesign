# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 13:54:37 2014

@author: Harshvardhan Bhatia
"""

from pattern.web import *

def dload_book(url):
    text = URL(x).download()
    bload = open(temp_load, w)
    bload.write(text)
    bload.close()
    
#def analysis():
    


# Main Code

url = str(raw_input('Enter your URL: '))      
dload_book(url)

    