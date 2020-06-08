# -*- coding: utf-8 -*-
"""
Created on Mon May  4 21:20:39 2020

@author: Sathwik Matcha
"""

def factorial(n):
    if(n==1):
        return 1
    else:
        return n*factorial(n-1)

N=100
str_N=str(factorial(N))
print(sum(list(map(int,list(str_N)))))