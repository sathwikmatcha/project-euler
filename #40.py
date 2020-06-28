# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 19:50:40 2020

@author: Sathwik Matcha
"""
import numpy as np

def special(d,diff):
    l=list(str(d))
    ans=l[len(l)-1-diff]
    ans=int(ans)
    return ans
def num_digits(n):
    l=list(str(n))
    return len(l)

cnt=0
d=1
cnt2=0
push=[1,10,100,1000,10000,100000,1000000]
ans_list=[]
while(True):
   
   num_d=num_digits(d)
   cnt+=num_d
   
   if(cnt >=push[cnt2]):
       
       diff=cnt-push[cnt2]
       ans1=special(d,diff)
       ans_list.append(ans1)
       cnt2+=1
   if(cnt2==len(push)):
       break
   d+=1    
   
print(ans_list)
print(np.prod(ans_list))