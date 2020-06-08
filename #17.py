# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 18:56:35 2020

@author: Sathwik Matcha
"""
import time
import inflect
p=inflect.engine()
def num_to_words(n):
    cnt=0
    word=p.number_to_words(n)
    words=list(word)
    cnt=0
    for i in range(len(words)):
        if(words[i]==' ' or words[i]=='-'):
            cnt+=1
    return (len(words)-cnt)
sum0=0
for i in range(1,1001):
    a=int(i)
    n=num_to_words(a)
    sum0+=n
print(sum0)
   