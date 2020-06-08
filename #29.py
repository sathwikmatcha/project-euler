# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 00:28:45 2020

@author: Sathwik Matcha
"""
import numpy as np



def make_set(n):
    A=np.zeros((99))
    for i in range(2,101):
        A[i-2]=pow(n,i)
    A=set(A)
    return A

N=100
N0=2

A2=0
'''2 oriented ops'''

set_2=make_set(2)
set_4=make_set(4)
set_8=make_set(8)

set_16=make_set(16)
set_32=make_set(32)
set_64=make_set(64)

set_24=set_2.union(set_4)

set_2_mega=(((set_24.union(set_8)).union(set_16)).union(set_32)).union(set_64)
A2+=len(set_2_mega)


'''3 oriented ops'''

set_3=make_set(3)
set_9=make_set(9)
set_27=make_set(27)
set_81=make_set(81)

set_3_mega=set_3.union(set_9).union(set_27).union(set_81)

A2+=len(set_3_mega)
'''5 oriented ops'''

set_5=make_set(5)
set_25=make_set(25)

set_5_mega=set_5.union(set_25)
A2+=len(set_5_mega)
'''6 oriented ops'''

set_6=make_set(6)
set_36=make_set(36)

set_6_mega=set_6.union(set_36)
A2+=len(set_6_mega)
'''7 oriented ops'''

set_7=make_set(7)
set_49=make_set(49)

set_7_mega=set_7.union(set_49)
A2+=len(set_7_mega)
'''10 oriented ops'''

set_10=make_set(10)
set_100=make_set(100)

set_10_mega=set_10.union(set_100)
A2+=len(set_10_mega)
A1=(99-18)*99
ans=A1+A2

print(ans)

