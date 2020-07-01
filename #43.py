# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 10:54:12 2020

@author: Sathwik Matcha
"""
def join_seq(l):
    l=[str(x) for x in l]
    l="".join(l)
    l=int(l)
    return l
def join(index,l):
    a=l[index]
    b=l[index+1]
    c=l[index+2]
    l1=[str(a),str(b),str(c)]
    d=int("".join(l1))
    return d
from itertools import permutations
r=list(range(10))

perm=permutations(r)
perm=list(perm)
sum0=0
prime_list=[2,3,5,7,11,13,17]

for i in perm:
    a=list(i)
    d0=1
    for j in range(len(prime_list)):
        d=join(j+1,a)
        if(d%prime_list[j]!=0 or a[0]==0):
            d0=0
            break
    if(d0!=0):
        sum0+=join_seq(a)
        print(join_seq(a))
        

print(sum0)                        