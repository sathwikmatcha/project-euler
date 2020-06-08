# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 13:04:31 2020

@author: Sathwik Matcha
"""
sum0=0
for i in range(1000):
    a=int(i)
    if(a%3==0 or a%5==0):
        sum0+=i
sum0=sum0
print(sum0)