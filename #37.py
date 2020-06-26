# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 22:41:58 2020

@author: Sathwik Matcha
"""
import numpy as np

def num_digits(n):
    s=str(n)
    l=list(s)
    num_d=len(l)
    return num_d
def stripper_left(s):
    del s[-1]
    a=int("".join(s))
    return a,s
def stripper_right(s):
    del s[0]
    a=int("".join(s))
    return a,s

def is_truncatable(n,L):
    if(n<10):
        return False
    else:
        num_d=num_digits(n)
        s1=list(str(n))
        s2=list(str(n))
        for i in range(num_d-1):
            a1,s1=stripper_left(s1)
            a2,s2=stripper_right(s2)
            if((a1 not in L) or (a2 not in L)):
                return False
        return True
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
            


cnt=0
N=pow(10,6)
sum0=0
L=sieve_of_eratosthenes(N)
for i in L:
    if(is_truncatable(i,L)):
        cnt+=1
        sum0+=i
print(cnt)
print(sum0)



