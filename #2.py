# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 16:29:00 2020

@author: Sathwik Matcha
"""
n=int(4*pow(10,6))
def f(i):
    if(i==1):
        return 1
    if(i==2):
        return 2
    else:
        return f(i-1)+f(i-2)
def even_fibonacci_sum(n):
    i=1
    m=f(i)
    sum0=0
    while(True):
        if(f(i)<=n):
            if(f(i)%2==0):
                sum0+=f(i)
            i+=1
        else:
            print(i)
            break
    print(sum0)
    
even_fibonacci_sum(n)