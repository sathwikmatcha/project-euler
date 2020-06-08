# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 16:16:45 2020

@author: Sathwik Matcha
"""
from fractions import Fraction

def abbc(a,c):
    m1=int(9*a*c)
    m2=int(10*a-c)
    statement=False
    if(m2!=0):
        m=int(m1/m2)
        m3=float(m1/m2)
        if(m3-m==0):
            frac=((10*a+m)/(10*m+c))
            if(frac<1 and m<10):
                statement=True
    return statement
'''ab/bc'''
a=[x for x in range(1,10)]
a=list(a)
c=[y for y in range(1,10)]
c=list(c)
frac_list=[]
for i in a:
    for j in c: 
        if(abbc(i,j)):
            m1=9*i*j
            m2=10*i-j
            m=int(m1/m2)
            frac=((10*i+m)/(10*m+j))
            print("i,j,m=",i,j,m)
            print(frac)
            frac_list.append(frac)
  
            
