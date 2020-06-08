# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 20:11:22 2020

@author: Sathwik Matcha
"""
def next_factorial(n,prev_factorial):
    return prev_factorial*n
def factorial(n):
    if(n>1):
        return n*factorial(n-1)
    else:
        return 1
def diff(n,f_list):
    n0=n
    n=list(str(n))
    n=[int(x) for x in n]
    ans=0
    for i in range(len(n)):
        ans+=f_list[n[i]]
    return ans-n0
N=50000
A=range(1,N)
f_list=[]
for i in range(10):
    f_list.append(factorial(i))
for i in A:
    if(diff(i,f_list)==0):
        print(i)