# -*- coding: utf-8 -*-
"""
Created on Tue May 17 22:52:51 2022

@author: Omotade
"""



import time
import crud



print('\nScheduling Start >>> \n Loading data into database every one hour \
      \n >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')


t = 3600 # wait time is 1 hr :60 minutes : 3600 seconds
while True:
    
    crud.load_data()
    now  = time.localtime()
    
    timestr = time.strftime('%a %I:%M %p', now)
    print("\nPrevoius Load Was at:> " + timestr)
    print('Next load in an hour...\n\n')
    
    # time sleep to delay the execution for an hour
    time.sleep(t)