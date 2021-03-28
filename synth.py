# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 17:27:30 2021

@author: Owner
"""
from pyo import *
import time



class Synth:
    def __init__(self,fadein=0.5,fadeout=0.5,dur=1,mul=0.5,weights=[8,0.2,5]):
        self.synth=self.get_synth(fadein,fadeout,dur,mul,weights) 
        self.dur=dur             

    def get_synth(self,fadein=0.5,fadeout=0.5,dur=1,mul=0.5,weights=[1,1,1]):
        f = Fader(fadein=fadein, fadeout=fadeout, dur=dur, mul=mul)
        saw = SuperSaw(freq=[100,100],detune=0.6, bal=0.8,mul=f*weights[0]).out()
        sine = Sine(freq=[100,100],mul=f*weights[1]).out()
        blit=Blit(freq=[100,100],mul=f*weights[2]).out()
        c=Mix([saw,sine,blit],voices=2).out()
        return f,saw,sine,blit,c
    
    def play(self,freq):
        for i in range(1,len(self.synth)-1):
            self.synth[i].setFreq([freq,freq])
        self.synth[0].play()
        #time.sleep(self.dur)
        



