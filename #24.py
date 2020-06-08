# -*- coding: utf-8 -*-
"""
Created on Mon May  4 23:31:07 2020

@author: Sathwik Matcha
"""
COUNT_ERROR=0
def factorial(n):
    if(n==0):
        return 1
    if(n==1):
        return 1
    else:
        return n*factorial(n-1)
def set_pos(n,a):

    a=reversed(a)
    ans_list=[]
    ans1=n
    for i in a:
        ans2=ans1//factorial(i)
        ans3=ans2*factorial(i)
        ans1=ans1-ans3
        ans_list.append(ans2)
    return ans_list
def shift(val,num):
    pass
    '''
    didn't make a proper function.Solved the answer using my own brain.
    '''
    
a=list(range(10))
print(a)
million=pow(10,6)
mi_pos=million-1
N0=million
print(set_pos(N0,a))