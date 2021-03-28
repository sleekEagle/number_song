# number_song

##Makking music with Irrational numbers
An irrational number cannot be expressed as a fraction or a finite number. 
The decimal places (if we write it down in decimal) goes on an on forever.
These numbers are apparently random.
This project tries to see if there is music in these numbers. 
Luckily NASA has calculates several square roots for a few millions of decimal places. 
e.g. https://apod.nasa.gov/htmltest/gifcity/sqrt2.1mil
So we use these. 

##read_file.py 
populates a buffer from the numbers read from the text file containing an irrational number 
such as sqrt(2)

##extract_interval_numbers.py
Creates melodies which changes rapidly and slowly. 
For the rapidly changing melodies, the numbers read from the data file is used (after some processing; described below).
For slower melodies, a moving average of the above values are used. 

##synth
This uses Pyo library from http://ajaxsoundstudio.com/software/pyo/
to generate sounds. We are using sine wave, inpulse train and saw tooth wave. 
All the parameters are configurabel in code. 

##main
Ties everything together. This gets numbers read from data file
and convert them to frequencies. For the base line, numbers are mapped to a 
lower frequency range. For lead parts, the numbers are mapped to a higher 
frequency range. 

##progression.txt
You can configure the progression of a song.
A single line from this file for example is,
10:1,0,1,0
The format of this is 
time:base,lead1,lead2,chord
This line describes the behaviour of the program till 10 seconds. 
base,lead1,lead2 and chord are Boolean values. 
if base=1, the song will have a base line till 10 seconds. 
If lead1=0, the song will not have a lead1 melody till 10 seconds. 
You can modify these values and conpose a simple song. 

This is at early development stage. Keep an eye out of updates. 
