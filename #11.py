# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 12:40:17 2020

@author: Sathwik Matcha
"""
def product(a=0,b=0,c=0,d=0):
    a=int(a)
    b=int(b)
    c=int(c)
    d=int(d)
    return a*b*c*d
def create_zero_edge_matrix(f):
    l0=len(f)
    l1=len(f[0])
    zero1=[0]*(l1+4)
    for i in range(l0):
        f[i].insert(0,0)
        f[i].insert(0,0)
        f[i].append(0)
        f[i].append(0)
    f.insert(0,zero1)
    f.insert(0,zero1)
    f.append(zero1)
    f.append(zero1)
def vertical_product_max(f):
    l0=len(f)
    l1=len(f[0])
    max_array_fin=[]
    for i in range(l0):
        max_array=[0]
        for j in range(l1):
              if(f[i][j]!=0):
                  a=f[i-1][j]
                  b=f[i][j]
                  c=f[i+1][j]
                  d=f[i+2][j]
                  ans1=product(a,b,c,d)
                  max_array.append(ans1)
        ans1=max(max_array)
        max_array_fin.append(ans1)
    ans=max(max_array_fin)
    return ans
def main_diagonal_product_max(f):
    l0=len(f)
    l1=len(f[0])
    max_array_fin=[]
    for i in range(l0):
        max_array=[0]
        for j in range(l1):
              if(f[i][j]!=0):
                  a=f[i-1][j-1]
                  b=f[i][j]
                  c=f[i+1][j+1]
                  d=f[i+2][j+2]
                  ans1=product(a,b,c,d)
                  max_array.append(ans1)
        ans1=max(max_array)
        max_array_fin.append(ans1)
    ans=max(max_array_fin)
    return ans
def other_diagonal_product_max(f):
    l0=len(f)
    l1=len(f[0])
    max_array_fin=[]
    for i in range(l0):
        max_array=[0]
        for j in range(l1):
              if(f[i][j]!=0):
                  a=f[i-1][j+1]
                  b=f[i][j]
                  c=f[i+1][j-1]
                  d=f[i+2][j-2]
                  ans1=product(a,b,c,d)
                  max_array.append(ans1)
        ans1=max(max_array)
        max_array_fin.append(ans1)
    ans=max(max_array_fin)
    return ans
def horizontal_product_max(f):
    l0=len(f)
    l1=len(f[0])
    max_array_fin=[]
    for i in range(l0):
        max_array=[0]
        for j in range(l1):
              if(f[i][j]!=0):
                  a=f[i][j-1]
                  b=f[i][j]
                  c=f[i][j+1]
                  d=f[i][j+2]
                  ans1=product(a,b,c,d)
                  max_array.append(ans1)
        ans1=max(max_array)
        max_array_fin.append(ans1)
    ans=max(max_array_fin)
    return ans
        
######################################################
file1=open("#11.txt","r")
f=[x.rstrip('\n').split() for x in file1.readlines()]
file1.close()
######################################################

create_zero_edge_matrix(f)

A=horizontal_product_max(f);
print(A)
B=vertical_product_max(f)
print(B)
C=main_diagonal_product_max(f)
print(C)
D=other_diagonal_product_max(f)
print(D)
x=(A,B,C,D)
print(max(x))