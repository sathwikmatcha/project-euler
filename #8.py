# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 20:06:42 2020

@author: Sathwik Matcha
"""

def product_man(a):
    prod=1
    for i in range(len(a)):
        a[i]=int(a[i])
        prod=prod*a[i]
    return prod
        
num1=str(73167176531330624919225119674426574742355349194934)
num2=str(96983520312774506326239578318016984801869478851843)
num3=str(85861560789112949495459501737958331952853208805511)
num4="12540698747158523863050715693290963295227443043557"
num5=str(66896648950445244523161731856403098711121722383113)
num6=str(62229893423380308135336276614282806444486645238749)
num7=str(30358907296290491560440772390713810515859307960866)
num8=str(70172427121883998797908792274921901699720888093776)
num9=str(65727333001053367881220235421809751254540594752243)
num10=str(52584907711670556013604839586446706324415722155397)
num11=str(53697817977846174064955149290862569321978468622482)
num12=str(83972241375657056057490261407972968652414535100474)
num13=str(82166370484403199890008895243450658541227588666881)
num14=str(16427171479924442928230863465674813919123162824586)
num15=str(17866458359124566529476545682848912883142607690042)
num16=str(24219022671055626321111109370544217506941658960408)

num17="07198403850962455444362981230987879927244284909188"

num18=str(84580156166097919133875499200524063689912560717606)
num19="05886116467109405077541002256983155200055935729725"
num20=str(71636269561882670428252483600823257530420752963450)
num=num1+num2+num3+num4+num5+num6+num7+num8+num9+num10+num11+num12+num13+num14+num15+num16+num17+num18+num19+num20
l=(list(num))
L=len(l)
a=13
prod_array=[]
for i in range(L-a):
    b=l[i:a+i]
    prod_array.append(product_man(b))
print(max(prod_array))