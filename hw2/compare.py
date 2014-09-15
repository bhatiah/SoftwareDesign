# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 17:48:34 2014

@author: harsh bhatia
"""

def compare(x, y):
    if x > y:
        return 1
    if x == y:
        return 0 
    if x < y:
        return -1 

x = raw_input('Enter x\n')
y = raw_input('Enter y\n')
x = int(x)
y = int(y)

z = compare(x, y)
print z
