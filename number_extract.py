# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 12:13:53 2021

@author: Owner
"""

import random
num_string = ''
for i in range(0,1000):
    n = random.randint(1,9)
    num_string+=str(n)
    
    




#a number between 0 and 99
num=99
def get_mapped(num,min_num,max_num,num_notes):
    period=(max_num-min_num)/num_notes

    mapped=0
    for i in range(1,num_notes+1):
        if(num<=period*i):
            mapped=i
            break
    return mapped





