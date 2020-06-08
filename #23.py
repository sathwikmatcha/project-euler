# -*- coding: utf-8 -*-
"""
Created on Mon May  4 23:06:54 2020

@author: Sathwik Matcha
"""
def two_sum_list(j,ab_list):
    ans1=ab_list[j]
    ans_list=[]
    for i in range(len(ab_list)):
        ans_list.append(ans1+ab_list[i])
    return ans_list
 
def proper_divisor_sum(n):
    ans=0
    for i in range(1,n):
        if(n%i==0):
            ans+=i
    return ans
def is_abundant(n):
    ans1=proper_divisor_sum(n)
    if(ans1>n):
        return True
    else:
        return False

N0=28123
abundant_list=[]

for i in range(1,N0+1):
    if(is_abundant(i)):
        abundant_list.append(i)
ans_list=[]
for i in range(len(abundant_list)):
    a_list=two_sum_list(i,abundant_list)
    ans_list+=a_list
ans_list=set(ans_list)
final_ans_list=[]
for i in range(1,N0+1):
    if not (i in ans_list):
        final_ans_list.append(i)
print(sum(final_ans_list))