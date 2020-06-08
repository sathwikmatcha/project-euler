# -*- coding: utf-8 -*-
"""
Created on Mon May  4 22:20:54 2020

@author: Sathwik Matcha
"""

from string  import ascii_lowercase

def score(string):
    string=string.replace('"','')
    string=string.replace("'","")
    string=string.lower()
    print(string)
    splitted=list(string)
    print(splitted)
    ans=0
    for i in splitted:
        a=ord(i)-96
        print(a)
        ans+=a
    return ans
file1=open("#22_names.txt","r")
a=file1.read().split(",")
a=list(map(str,a))
a=sorted(a)
print(a)
file1.close()
ans=0
for i in range(len(a)):
    string=a[i]
    score_of_string=score(string)
    print(string,score_of_string,i)
    ans+=score_of_string*(i+1)

print("")
print(score(a[0]))
print(ans)