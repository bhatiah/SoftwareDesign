# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 17:40:03 2014

@author: harsh
"""
from pattern.web import *

bload = open('words.txt', 'w')
bload.write(plaintext(URL('http://www.readingrockets.org/article/basic-spelling-vocabulary-list').download()))
bload.close()
