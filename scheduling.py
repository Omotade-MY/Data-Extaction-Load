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
    tm = time.localtime(time.time())
    
    
    print("\nPrevoius Load Was at:> {}:{}".format(tm.tm_hour,tm.tm_min))
    print('Next load in an hour...')
    
    # time sleep to delay the execution for an hour
    time.sleep(t)