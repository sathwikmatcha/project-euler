z=open("#42_names.txt","r")
f1=z.readline()
f1=f1.split(",")
f1=[x.strip("\"").lower() for x in f1]
z.close()

def tri_check(n):
    base=0
    i=1
    while(True):
        base=base+i
        if(base<n):
            i+=1
            continue
        if(base==n):
            return True
        if(base>n):
            return False

def make_sum(word):
    
    word=list(word)
    ans_list=[(ord(x)-96) for x in word]
    return sum(ans_list)

i=0
ans=0



while(i<len(f1)):
    ans1=make_sum(f1[i])
    if(tri_check(ans1)):
        ans+=1
    i+=1

print(ans)