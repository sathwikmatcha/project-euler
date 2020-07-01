# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 06:05:27 2020

@author: Sathwik Matcha
"""
def is_pentagonal(n):
    base=1
    cnt=1
    while(True):
        if(base<n):
            inc=3*cnt+1
            base=base+inc
            cnt+=1
            continue
        if(base==n):
            return True
        else:
            return False
        
        
    

def pentagon_num(n):
    ans=(n*(3*n-1))//2
    return ans

i=1
j=1
ans=0
state=0

while(True):
    num1=pentagon_num(i)
    j=i
    cnt=0
    while(cnt<3*i//2):
        num2=pentagon_num(j)
        if(num2==num1):
            j+=1
            continue
        if(is_pentagonal(num1+num2)):
            print("Sum True: ",i,j,num1,num2,num1+num2)
            if(is_pentagonal(num2-num1)):
                print("diff true: ",i,j,num2-num1)
                break
        j+=1
        cnt+=1        
    if(state==1):
        break
    i+=1

print("")
print("")
print("")
print(ans)