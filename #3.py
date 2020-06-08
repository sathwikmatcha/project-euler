# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 16:40:50 2020

@author: Sathwik Matcha
"""
N=int(600851475143)
def prime_factor(N):
    a=0
    for i in range(2,10000):
        if(N%i==0):
            print(i)
            a=N/i;
            print(a)
            if(a==1):
                return N
            else:
                prime_factor(a)
print(prime_factor(N))