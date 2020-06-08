# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 01:16:37 2020

@author: Sathwik Matcha
"""
def sol_ab(sum0):
    return ((sum0+1)-((sum0+1)//2))
cnt=0
iterations=0
for i1 in range(0,201,200):
    for i2 in range(0,201,100):
        for i3 in range(0,201,50):
            for i4 in range(0,201,20):
                for i5 in range(0,201,10):
                    for i6 in range(0,201,5):
                        iterations+=1
                        sum_=i1+i2+i3+i4+i5+i6
                        if(sum_<=200):
                            sum0=200-sum_
                            cnt+=sol_ab(sum0)

print("")
print("")                                     
print(cnt)
print(iterations)