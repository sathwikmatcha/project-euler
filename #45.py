# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 10:56:14 2020

@author: Sathwik Matcha
"""
from math import sqrt
def triangular_num(n):
    ans=(n*(n+1))//2
    return ans
def tri_hex_check(n):
    if(n%2==1):
        return True,((n+1)//2)
    else:
        return False,0 
def tri_pent_check(n):
    if(n==0):
        return False,0
    else:
        ans=1+12*(n+1)*n
        ans=sqrt(ans)
        ans2=(ans*n+n)/(6*n*n)
        if(n*ans==int(n*ans) and n*ans2==int(n*ans2)):
            return (True,n*ans2)
        else:
            return (False,0)
i=0
cnt=0
temp=0
ans_list=[]
while(cnt<3):
    a,b=tri_pent_check(i)
    if(a):
        c,d=tri_hex_check(i)
        if(c):
            temp=i
            print(temp,b,d)
            ans_list.append(temp)
            cnt+=1
    i+=1
print(temp)
print(triangular_num(temp))
print(ans_list)