# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 20:44:51 2020

@author: Sathwik Matcha
"""
import numpy as np
from itertools import permutations
from time import time

def circular_check(a,list_):
    A=set(permutations_num(a))
    statement=True
    if(len(list_.intersection(A))!=len(A)):
        statement=False
    return statement

def permutations_num(n):
    '''
    gives the list of permutations of a prime number n
    '''
    n=list(str(n))
    n=[int(x) for x in n]

    perm=permutations(n)
    
    str_=[]
    for i in perm:
        j=str(i)
        j=j.strip("(").strip(")")
        k=[(x.strip(" ")) for x  in j.split(",")]
        k=int("".join(k))
        str_.append(k)

    return str_

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


t1=time()
n=pow(10,6)
cnt=0



list_1000000=set(sieve_of_eratosthenes(1000000))
print(list_1000000)

for i in sieve_of_eratosthenes(n):
    if(circular_check(i,list_1000000)):
        cnt+=1


t2=time()
print(cnt)
print("")
print("time taken =",(t2-t1),"ms")            
