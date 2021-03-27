# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 18:02:25 2021

@author: Owner
"""
import threading
import time


number_list=[]

data = open('C:/Users/Owner/code/number_song/sqrt3.txt', 'r')
def populate_number_list(stop,allowed_len):
    print('started...')
    number=''            
    while True:
        if stop():
            print('killing thread')
            break
        if(len(number_list)<allowed_len):
            if(len(number)==2):
                number_list.append(int(number))
                number=''
            
            char=data.read(1)
            if(char.isdigit()):
                number+=char
        time.sleep(0.001)

stop_populate=True
stop_populate=False
t1 = threading.Thread(target = populate_number_list, args =((lambda : stop_populate,500)))
t1.start()