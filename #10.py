# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 21:42:56 2020

@author: Sathwik Matcha
"""
#####################################
from math import sqrt
from time import time
N=2*pow(10,6)
#####################################
def sieve_of_eratosthenes(n):                   #RETURNS sum of primes
    prime_array=[1]*(n+1)                     #base array
    prime_array[0]=0;prime_array[1]=0;
    i=1
    ans=[]                                      #1,0 assignment
    while(i<n):
        if(prime_array[i]==1):
            j=2;
            ans.append(i)
            print(i)
            while(i*j<=n):
                prime_array[i*j]=0
                j+=1
                continue
            i+=1
            continue
        else:
            i+=1
            continue
    return sum(ans)
####################################
t1=time()

print(sieve_of_eratosthenes(N))
t2=time()
t=t2-t1
t=round(t,7)
print(t)