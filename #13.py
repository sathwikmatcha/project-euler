# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 10:49:12 2020

@author: Sathwik Matcha
"""

f1=open("#13.txt","r")
list0=f1.readlines()
f1.close()
for i in range(len(list0)):
    list0[i]=int(list0[i].rstrip('\n'))
    print(list0[i])
print("")
ans1=sum(list0)
ans1=str(ans1)
print(ans1)
ans1=list(ans1)
l=len(ans1)
print("".join(ans1[:10]))