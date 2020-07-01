# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 14:32:43 2020

@author: Sathwik Matcha
"""
from math import sqrt

def triangular_num(n):
    ans= (n*(n+1))//2
    return ans

def div_num(n):
    s=sqrt(n)
    s_int=int(s)
    cnt=0
    ans=0
    for i in range(1,s_int+1):
        if(n%i==0):
            cnt+=1
    ans=2*cnt
    if(s==int(s)):
        ans-=1
                
    return ans

divisors=0
i=1
ans=0
while(divisors<=500):
    t=triangular_num(i)
    if(div_num(t)>500):
        print(i,t,div_num(t))
        ans=t
        break
    else:
        print(i,t,div_num(t))
        i+=1
            
print(ans)
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   