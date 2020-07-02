# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 15:33:58 2020

@author: Sathwik Matcha
"""
def factorial(n): 
    if n < 0: 
        return 0
    elif n == 0 or n == 1: 
        return 1
    else: 
        fact = 1
        while(n > 1): 
            fact *= n 
            n -= 1
        return fact 

def C(n,r):
    return factorial(n)//(factorial(n-r)*factorial(r))

def rem(a,b,base):
    r=a-b
    factor=pow(a,r)
    main=pow(b,10)
    cnt=9
    sum0=0
    while(cnt>=0):
        f=factor*C(b,b-cnt)*main//pow(b,10-cnt)
        f1=int(f%base)
        if(f1==0):
            f=0
            sum0+=f
            cnt-=1
            continue
        else:
            sum0+=f
            cnt-=1
            continue
    ans=sum0
    return int(ans)

base=pow(10,10)
N0=10405071317

i=11
ans1=N0
while(i<=1000):
    
    if(i%10==0):
        i+=1
        continue
    else:
        b=(i//10)*10
        ans2=rem(i,b,base)
        print("ans2= ",ans2)
        ans1+=ans2
        ans1=ans1
        print("ans1= ",ans1)
        i+=1 
        continue

print("")
print("")
print("")
print("")
print("")
print("")
print(ans1%base)