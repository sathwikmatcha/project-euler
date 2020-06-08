# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 16:55:45 2020

@author: Sathwik Matcha
"""
def next_collatz(n):
    if(n%2==0):
        return n//2
    if(n%2==1):
        return 3*n+1
    if(n==1):
        return 1
def len_collatz(N):
    cnt=0
    while(True):
        if(N==1):
            cnt=0
            break
        else:
            N=next_collatz(N)
            cnt+=1
            if(N==1):
                break
            continue
    return cnt+1
N=pow(10,6)
i=1
ans_array=[]
maximum=0
imax=0
while(i<N):
    m=len_collatz(i)
    ans_array.append(m)
    print(i,m)
    if(m>maximum):
        imax=i
        maximum=m
    i+=1
    continue
print(imax)    