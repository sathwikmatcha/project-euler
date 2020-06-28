# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 16:47:34 2020

@author: Sathwik Matcha
"""
import numpy as np
l=1001
cnt_list=[0]*l
cache=[]
M=0
ans=0
for m in range(1,l):
    for n in range(1,l):
        c=(m*m)+(n*n)
        a=(m*m)-(n*n)
        b=2*m*n
        
        if(a<=0 or c<a or c<b):
            break
        
        elif(a+b+c>1000):
            break
        
        else:
            p=a+b+c
            print(a,b,c,p)
            cache.append([a,b,c,p])
            cnt_list[p]+=1
            if(a==b):
                cnt_list[p]-=1
print(cnt_list)
ans_list=[]
print(max(cnt_list))
for i in range(1001):
    if(cnt_list[i]==max(cnt_list)):
        ans_list.append(i)

print(ans_list)