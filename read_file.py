# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 18:02:25 2021

@author: Owner
"""
import threading
import time


class ReadFile:
    def __init__(self, max_buffer_len,data_file):
        self.number_list=[]
        self.data=data = open(data_file, 'r')
        self.max_buffer_len=max_buffer_len
        self.stop_populate=False
        self.t1 = threading.Thread(target = self.populate_number_list, args =((lambda : self.stop_populate,self.max_buffer_len)))
        
    def populate_number_list(self,stop,allowed_len):
        print('started file reading thread')
        number=''            
        while True:
            if stop():
                print('killing file reading thread')
                break
            if(len(self.number_list)<self.max_buffer_len):
                if(len(number)==2):
                    self.number_list.append(int(number))
                    number=''
                
                char=self.data.read(1)
                if(char.isdigit()):
                    number+=char
            time.sleep(0.001)
            
    def get_number(self):
        try:
            return self.number_list.pop(0)
        except Exception as e:
            print(e)
            return -1
    
    def start_thread(self):
        self.stop_populate=False
        self.t1.start()
    
    def kill_thread(self):
        self.stop_populate=True
        



