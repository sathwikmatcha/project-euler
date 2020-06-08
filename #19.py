# -*- coding: utf-8 -*-
"""
Created on Mon May  4 19:54:28 2020

@author: Sathwik Matcha
"""

import datetime
cnt=0
day=1
month=1
year=1901
while(year<=2000):
    month=1
    while(month<=12):
        today=datetime.datetime(year,month,day)
        whichday=today.weekday()
        if(whichday==6):
            cnt+=1
        month+=1
        continue
    year+=1
print(cnt)