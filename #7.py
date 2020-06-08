# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 18:45:14 2020

@author: Sathwik Matcha
"""
def next_prime(a):
    ans=a+1
    while(True):
        if(is_prime(ans)):
            return ans
        else:
            ans+=1
def is_prime(a):
    cnt=0
    if(a%2==0 and a>2):
        return False
    if(a%3==0 and a>3):
        return False
    for i in range(2,a//2+1):
        if(a%i!=0):
            cnt+=1
    if(cnt==a//2-1):
        return True
def prime(a):
    ans=a
    i=0
    while(True):
        if(is_prime(ans)):
            i+=1
            if(i==10000):
                return ans
                break
            ans+=1
            continue
        else:
            ans+=1
            continue
p=2
p=prime(p)
p=next_prime(p)
print(p)
