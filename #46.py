# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 11:49:24 2020

@author: Sathwik Matcha
"""
from math import sqrt

def goldbach_conjecture(n):
    a=int(sqrt((n-3)//2)+1)
    for i in range(1,a):
        b=n-2*i*i
        if (is_prime(b)):
            return True
    return False

def is_prime(i):
    a=int(sqrt(i)+1)
    for j in range(2,a+1):
        if(i%j==0):
            return False
    return True

def odd_composite(i):
    if not(is_prime(i)):
        if(i%2==1):
            return True
    return False

i=3
ans=0
while(True):
    if(odd_composite(i)):
        print("Cv: ",i)
        if not(goldbach_conjecture(i)):
            ans=i
            break
    i+=1

print(ans)
