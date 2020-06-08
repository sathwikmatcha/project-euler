# -*- coding: utf-8 -*-
"""
Created on Mon May  4 21:27:12 2020

@author: Sathwik Matcha
"""


def proper_divisors_list(n):
    ans_list=[]
    for i in range(1,n):
        if(n%i==0):
            ans_list.append(i)
    return ans_list
N=10000
i=2
ans_list=[]
while(i<N):
    sum_proper_1=sum(proper_divisors_list(i))
    sum_proper_2=sum(proper_divisors_list(sum_proper_1))
    if(i==sum_proper_2 and i!=sum_proper_1):
        print(i,sum_proper_1)
        ans_list.append(i)
    i+=1
    continue

print(ans_list)
ans=sum(ans_list)

print(ans)
    