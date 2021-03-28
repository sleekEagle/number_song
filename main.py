# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 00:05:02 2021

@author: Owner
"""


import extract_interval_numbers    
        
        

file='C:/Users/Owner/code/number_song/sqrt3.txt'    
take_avg_of=[1,2,3,4]        
pop=extract_interval_numbers.PopulateNumbers(file,take_avg_of,10000)
pop.start_thread()
pop.get_numbers(1)
pop.kill_thread()
pop.num_lists[0]

len(pop.p.number_list)


[l.pop(0) for l in num_lists]
i=2
num_lists[i].pop(0)
