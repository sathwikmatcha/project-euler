# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 17:32:43 2020

@author: Sathwik Matcha
"""
def palindrome(n):
    str_a=list(str(n))
    l=len(str_a)
    str_b=[]
    for i in range(len(str_a)):
        str_b.append(str_a[l-1-i])
    if(int("".join(str_b))==n):
        return True
    else:
        return False
x=0;m=[]
for i in range(100,1000):
    for j in range(100,1000):
        if (palindrome(i*j)):
            x=i*j
            m.append(x)

print(max(m))