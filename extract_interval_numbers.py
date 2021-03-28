# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 19:38:11 2021

@author: Owner
"""


import read_file
import time
import threading

class PopulateNumbers:
    def __init__(self,file,take_avg_of,max_buffer_len):
        #start file reading thread
        print('starting file reading thread....')
        self.p=read_file.ReadFile(max_buffer_len*2,file)
        self.p.start_thread()
        #sleep till a significant number of data is read from file
        time.sleep(1)

        self.take_avg_of=take_avg_of
        self.max_buffer_len=max_buffer_len
        self.counter_list=counter_list=[0]*(len(take_avg_of))
        self.num_lists=[]
        for i in range(len(take_avg_of)):
            self.num_lists.append([])
            
        self.stop_populate=False
        self.t1 = threading.Thread(target = self.populate_numbers, args =[lambda : self.stop_populate])
                
        
            
    def populate_numbers(self,stop):
        print('starting populate numbers...')
        while True:
            try:
                if stop():
                    print('killing number populating thread')
                    break
                if((len(self.num_lists[0])<self.max_buffer_len) and (len(self.p.number_list)>30)):
                    num=self.p.get_number()
                    self.num_lists[0].append(num)
                    self.counter_list=[item+1 for item in self.counter_list]
                    self.counter_list[0]=0
                    
                    index_list=[i for i,item in enumerate(self.counter_list) if (i!=0) and (item==self.take_avg_of[i])]
                        
                    for index in index_list:
                            values=self.num_lists[0][-1*self.take_avg_of[index]:]
                            mean=sum(values)/len(values)
                            self.num_lists[index].append(mean)
                            self.counter_list[index]=0
                time.sleep(0.01)
            except Exception as e:
                time.sleep(1)
                print(e)
                
    def get_num_lists(self):
        return self.num_lists
    
    def start_thread(self):
        self.stop_populate=False
        self.t1.start()
    
    def kill_thread(self):
        self.p.kill_thread()
        self.stop_populate=True
    #pop first item of the i_th list of num_lists
    def get_numbers(self,i):
        try:
            return self.num_lists[i].pop(0)
        except Exception as e:
            print(e)
            return -1






