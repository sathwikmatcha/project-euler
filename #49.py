# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 19:07:12 2020

@author: Sathwik Matcha
"""

import numpy as np
from itertools import permutations




def sieve_of_eratosthenes(n):

    A=np.ones((n+1))

    A[0]=0
    A[1]=0

    i=2

    prime_list=[]

    while(i<n):

        if(A[i]==1):
            prime_list.append(i)

            g=2

            while(g*i<=n):

                A[g*i]=0
                g+=1

                continue

            i+=1
            continue

        else:

            i+=1
            continue


    return prime_list

def perm_prime(i,A):
    l=list(str(i))
    perm=permutations(l)
    perm=list(perm)
    perm=[int("".join(x)) for x in perm]
    ans_list=[]
    for j in range(len(perm)):
        if(perm[j]<1000):
            perm[j]=0
        elif not(perm[j] in A):
            perm[j]=0
        else:
            ans_list.append(perm[j])
    return ans_list
N=10000

A=sieve_of_eratosthenes(N)
#print(A)

for i in range(len(A)):
    if(A[i]<1000):
        A[i]=0
ans_list=[]
print(perm_prime(1013,A))
for i in range(len(A)):
    j=perm_prime(A[i],A)
    
    if(len(j)==3):
        print(j)
        if(j[0]+j[2]==2*j[1]):
            ans_list.append(j)

print(min(ans_list))
ans1=perm_prime(min(ans_list),A)
ans1=[str(x) for x in ans1]
answer="".join(ans1)
print(answer)
