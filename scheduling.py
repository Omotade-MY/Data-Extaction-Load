# -*- coding: utf-8 -*-
"""
Created on Tue May 17 22:52:51 2022

@author: Omotade
"""


import time
import crud



print('\nScheduling Start >>> \n Loading data into database every one hour \
      \n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
# start time is in minutes

t = 90 # wait time is 1 hr :60 minutes
while True:
    
    crud.load_data()
    tm = time.localtime(time.time())
    # time sleep to delay the execution for an hour
    print("\nPrevoius Load Was at:> {}:{}".format(tm.tm_hour,tm.tm_min))
    print('Next load in an hour...')
    
    time.sleep(t)