# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 22:16:24 2020

@author: Sathwik Matcha
"""
import copy
def is_palindrome(n):
    s=str(n)
    b=list(s)
    c=copy.deepcopy(b)
    b.reverse()
    if(c==b):
        return True
    else:
        return False
def is_bin_palindrome(n):
    bin_str=str(bin(n).replace("0b",""))
    bin_int=int(bin_str)
    if(is_palindrome(bin_int)):
        return True
    else:
        return False
N=pow(10,6)

i=1
sum0=0
while(i<=N):
    if(is_palindrome(i)):
        if(is_bin_palindrome(i)):
            sum0+=i    
    i+=1
print(sum0)
