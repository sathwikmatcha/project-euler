# -*- coding: utf-8 -*-
"""
Created on Tue May  5 00:37:38 2020

@author: Sathwik Matcha
"""
from time import time
def no_of_digits(n):
    return len(list(str(n)))
def updated_fibonacii(store_fibonacii,new_fibonacci):
    new_fibonacci=fibonacci_optimized(store_fibonacci)
    store_fibonacci[0]=store_fibonacci[1]
    store_fibonacci[1]=new_fibonacci
    return store_fibonacii
def fibonacci_optimized(store_fibonacci):
    return sum(store_fibonacci)
store_fibonacci=[1,1]
index=2
init_time=time()
while(True):
    new_fibonacci=fibonacci_optimized(store_fibonacci)

    index+=1
    if(no_of_digits(new_fibonacci)>=1000):
        print(index)
        break
    else:
        store_fibonacii=updated_fibonacii(store_fibonacci,new_fibonacci)
        continue
final_time=time()
print(final_time-init_time)
