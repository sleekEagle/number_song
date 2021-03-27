# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 17:27:30 2021

@author: Owner
"""

from pyo import *
# Set Up Server
s = Server()
s.setMidiInputDevice(2) # Must be called before s.boot()
s.boot()
s.start()

a = Sine(mul=0.1).out()

wave = SquareTable()
osc = Osc(wave, freq=1111, mul=5)

# FX
verb = Freeverb(osc).out()

s.stop()
