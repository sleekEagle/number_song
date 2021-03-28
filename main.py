# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 19:38:11 2021

@author: Owner
"""


import read_file
import time


file='C:/Users/Owner/code/number_song/sqrt3.txt'


p=Populate(500,file)
p.start_populating()
len(p.number_list)
p.get_number()
p.kill_populating()

#minimum interval between two notes played in seconds
min_interval=0.5
take_avg_of=[1,2,3,4]
counter_list=[0]*(len(take_avg_of))
#we need one more list to hold the fastest notes
num_lists=[]
for i in range(len(take_avg_of)):
    num_lists.append([])

while True:
    num=p.get_number()
    num_lists[0].append(num)
    counter_list=[item+1 for item in counter_list]
    counter_list[0]=0
    
    index_list=[i for i,item in enumerate(counter_list) if (i!=0) and (item==take_avg_of[i])]
        
    for index in index_list:
            values=num_lists[0][-1*take_avg_of[index]:]
            mean=sum(values)/len(values)
            num_lists[index].append(mean)
            counter_list[index]=0
    time.sleep(1)
    print(num_lists)
    
