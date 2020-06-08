# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 23:36:39 2020

@author: Sathwik Matcha
"""

N=1001

i=1

sum1=0
sum2=0
sum3=0
sum4=0

while(True):
    t1=i*i
    t11=i+1
    t2=t1+t11
    t3=t1+2*t11
    t4=t1+3*t11
    sum1+=t1
    sum2+=t2
    sum3+=t3
    sum4+=t4
    print(t1,t2,t3,t4)
    if(i==N):
        sum2-=t2
        sum3-=t3
        sum4-=t4
        break
    else:
        i+=2
        continue

ans=sum1+sum2+sum3+sum4
print(ans)