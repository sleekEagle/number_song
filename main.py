# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 00:05:02 2021

@author: Owner
"""


import extract_interval_numbers  
import synth  
from pyo import *
import time
import os

def get_mapped_value(val,val_min=0,val_max=99,map_min=20,map_max=2000):
    m=(map_max-map_min)/(val_max-val_min)
    c=map_max-m*val_max
    mapped=m*val+c
    return mapped  

def main():
    #setting up file paths
    dir = os.path.dirname(synth.__file__)
    progression_file=os.path.join(dir, 'progression.txt')
    sqrt_file=os.path.join(dir, 'sqrt3.txt')


    #read parameters
    f = open(progression_file, "r")
    lines=f.readlines()
    progression=[]
    for item in lines:
        t=item.split(':')[0]
        play=(item.split(':')[-1])[0:7].split(',')
        progression.append([t,play])
    
      
     

    #these are for chord,lead,lead2,base   
    take_avg_of=[1,2,3,16]        
    pop=extract_interval_numbers.PopulateNumbers(sqrt_file,take_avg_of,10000)
    time.sleep(1)
    pop.start_thread()
    time.sleep(1)
    pop.get_numbers(0)


    s = Server().boot()
    s.start()
    
    base=synth.Synth(fadein=0.02,fadeout=0.02,dur=1.6,mul=0.5,weights=[0.08,0.8,0.2])
    lead2=synth.Synth(fadein=0.3,fadeout=0,dur=0.3,mul=0.5,weights=[0.8,0.1,0.1])
    lead=synth.Synth(fadein=0,fadeout=0.2,dur=0.2,mul=0.5,weights=[0.6,0.2,0.1])
    chord=synth.Synth(fadein=0.01,fadeout=0.09,dur=0.1,mul=0.5,weights=[0.5,0.8,0.1])
    synth_list=[chord,lead,lead2,base]
      
    count=0
    while True:
        t=count*0.1
        if(t>=int(progression[-1][0])):
            break
        prog_index=[i for i,p in enumerate(progression) if t<int(p[0])][0]
        is_base,is_lead,is_lead2,is_chord=progression[prog_index][1]
        if(count%take_avg_of[0]==0):
            num=pop.get_numbers(0)
            num=get_mapped_value(num,val_min=0,val_max=99,map_min=240,map_max=720)
            if(int(is_chord)):
                chord.play(num)
            time.sleep(0.1)
           
        if(count%take_avg_of[1]==0):
            num=pop.get_numbers(1)
            num=get_mapped_value(num,val_min=0,val_max=99,map_min=80,map_max=240)
            if(int(is_lead)):
                lead.play(num)
        
        if(count%take_avg_of[2]==0):
            num=pop.get_numbers(2)
            num=get_mapped_value(num,val_min=0,val_max=99,map_min=40,map_max=120)
            if(int(is_lead2)):
                lead2.play(num)
          
        if(count%take_avg_of[3]==0):
            num=pop.get_numbers(3)
            num=get_mapped_value(num,val_min=0,val_max=99,map_min=20,map_max=60)
            if(int(is_base)):
                base.play(num)
            
        count+=1
    


if __name__ == "__main__":
    main()



















