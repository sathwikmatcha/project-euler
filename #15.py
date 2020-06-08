# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 17:48:32 2020

@author: Sathwik Matcha
"""

def factorial(n):
    if(n==1):
        return 1
    else:
        return n*factorial(n-1)
a=(factorial(40))
b=factorial(20)
ans=int(a/b**2)
print(ans)