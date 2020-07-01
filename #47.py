# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 14:43:05 2020

@author: Sathwik Matcha
"""

def prime_sequence(n):

    ans_list=[]
    i=2

    while(i<=n):

        if(n%i==0):
    
           n=n/i
           
           if(i not in ans_list):
               ans_list.append(i)
           continue
       
        if(n%i!=0):
            i+=1
            continue
        if(n<i):
            break
    
    return len(ans_list)

def consecutive_num(n0,n1,n):
    r=range(n,n+n0)
    ans0=prime_sequence(n)
    if(n1!=ans0):
        return False
    for i in r:
        if(prime_sequence(i)!=ans0):
            return False
    return True

i=2
ans=0
print("102: ",prime_sequence(102))
while(True):
    if(consecutive_num(4,4,i)):
        ans=i
        break
    print(i,"prime_nums in it: ",prime_sequence(i))
    i+=1
    
print(ans)
print(prime_sequence(ans))