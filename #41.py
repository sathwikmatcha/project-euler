from itertools import permutations
import numpy as np
r1=list(range(4,0,-1))
r2=list(range(7,0,-1))
def sieve_of_eratosthenes(n):

    A=np.ones((n+1))

    A[0]=0
    A[1]=0

    i=2

    prime_list=[]

    while(i<n):

        if(A[i]==1):
            prime_list.append(i)

            g=2

            while(g*i<=n):

                A[g*i]=0
                g+=1

                continue

            i+=1
            continue

        else:

            i+=1
            continue


    return prime_list

N=pow(10,8)
A=sieve_of_eratosthenes(N)
A.reverse()

perm2=permutations(r2)
perm2=list(perm2)

answer=0

for i in perm2:
    a=list(i)
    a=[str(x) for x in i]
    a="".join(a)
    a=int(a)
    if(a in A):
        answer=a
        del perm2
        break
    else:
        continue
    

print(answer)