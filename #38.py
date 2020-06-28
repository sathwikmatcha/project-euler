# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 15:29:48 2020

@author: Sathwik Matcha
"""
def convert_num_to_set(a):
    s=list(str(a))
    s1=set(s)
    if(len(s1)==len(s)):
        return s
    else:
        return None
N=99999

set_standard={"1","2","3","4","5","6","7","8","9"}
i=1
ans=0
ans_list=[]
while(i<N):
   j=1
   s=set()
   while(len(s)<=9):
       product=i*j
       s1=convert_num_to_set(product)
       if(s1==None):
           break
       if("0" in s1):
           break
       su=s.union(s1)
       si=s.intersection(s1)
       if(len(si)>0):
           break
       else:
           if(su==set_standard):
               ans=i
               ans_list.append(i)
               break
           else:
               s=su
               j+=1
    
   i+=1
print(ans_list)
print(ans)