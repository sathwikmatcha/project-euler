# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 14:32:43 2020

@author: Sathwik Matcha
"""
from time import time
def power_sequence(n,prime):
    power=[]
    l=len(prime)
    i=0
    while(i<l):
        j=0;a=0
        while(True):
            p=pow(prime[i],j+1)
            if(n%p!=0):
                a=j
                break
            else:
                j+=1
                continue
        power.append(a)
        i+=1
    return power
def sieve_of_eratosthenes(n):
    prime_array=[]
    if(n==1):
        return prime_array
    prime_base=[1]*(n+1)
    prime_base[0]=0;prime_base[1]=0
    i=1
    while(i<=n):
        if(prime_base[i]==1):
            j=2
            if(n%i==0):
                prime_array.append(i)
            while(i*j<=n):
                prime_base[i*j]=0
                j+=1
                continue
            i+=1
            continue
        else:
            i+=1
            continue
    print(prime_array)
    return prime_array
def num_of_factors(power):
    product=1
    for i in range(len(power)):
        product=product*(power[i]+1)
    return product
def triangle_number(n):
    x=int(n*(n+1)/2)
    return x
N=2610
t1=time()
while(True):
   N2=triangle_number(N)
   x=sieve_of_eratosthenes(N2)
   y=power_sequence(N2,x)
   ans1=num_of_factors(y)
   print(N,N2,ans1)
   if(ans1>500):
       print("")
       print(N2)
       print(ans1)
       break
   else:
       N+=1
       continue
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   