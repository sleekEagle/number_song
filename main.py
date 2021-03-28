# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 00:05:02 2021

@author: Owner
"""


import extract_interval_numbers  
import synth  
from pyo import *
import time


        
def get_mapped_value(val,val_min=0,val_max=99,map_min=20,map_max=2000):
    m=(map_max-map_min)/(val_max-val_min)
    c=map_max-m*val_max
    mapped=m*val+c
    return mapped       

file='C:/Users/Owner/code/number_song/sqrt3.txt' 
#these are for chord,lead,lead2,base   
take_avg_of=[1,2,3,16]        
pop=extract_interval_numbers.PopulateNumbers(file,take_avg_of,10000)
pop.start_thread()
pop.get_numbers(0)
pop.kill_thread()
pop.num_lists[0]

s = Server().boot()
s.start()

base=synth.Synth(fadein=0,fadeout=0,dur=1.6,mul=0.5,weights=[0.9,0.5,5])
lead2=synth.Synth(fadein=0,fadeout=0,dur=0.3,mul=0.5,weights=[0.9,0.5,5])
lead=synth.Synth(fadein=0,fadeout=0,dur=0.2,mul=0.5,weights=[0.9,0.5,5])
chord=synth.Synth(fadein=0,fadeout=0,dur=0.1,mul=0.5,weights=[0.9,0.5,5])
synth_list=[chord,lead,lead2,base]


counter_list=counter_list=[0]*(len(take_avg_of))
while True:
    for i,item in enumerate(counter_list):
        if(item==0):
            num=pop.get_numbers(i)
            synth_list[i].play(num)
    counter_list=[item+1 for item in counter_list]
    index_list=[i for i,item in enumerate(counter_list) if (i!=0) and (item==take_avg_of[i])]                   
    for index in index_list:
        counter_list[index]=0
    time.sleep(0.1)
            
    
    index_list=[i for i,item in enumerate(counter_list) if (i!=0) and (item==take_avg_of[i])]                   
    for index in index_list:
        counter_list[index]=0
    time.sleep(1.6)
       


get_mapped_value(99,val_min=0,val_max=99,map_min=100,map_max=1000)


base.play(45)
print(21)
lead.play(300)


    
























