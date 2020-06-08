# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 20:40:42 2020

@author: Sathwik Matcha
"""

a=0;b=0;c=0;
x=(a,b,c)
m=2;n=1
while(True):
    while(True):
        if(m>n):
            a=m*m-n*n
            print(a,end=" ")
            b=2*m*n
            print(b,end=" ")
            c=m*m+n*n
            print(c)
            n+=1
            if(a+b+c==1000):
                break
            continue
        else:
            m+=1
            n=1
            break
    if(a+b+c==1000):
        print(a*b*c)
        break
print(ans)
        