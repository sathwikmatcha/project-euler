import numpy as np

file1=open("#18.txt","r")
f=file1.readlines()
f=[x.strip("\n").split() for x in f ]
file1.close()
def initial_sum_list(mini_pyramid):
    
    S=np.zeros((3))
    
    S[0]=mini_pyramid[0,0]+mini_pyramid[1,0]+mini_pyramid[2,0]
    S[1]=max(mini_pyramid[0,0]+mini_pyramid[1,0]+mini_pyramid[2,1],mini_pyramid[0,0]+mini_pyramid[1,1]+mini_pyramid[2,1])
    S[2]=mini_pyramid[0,0]+mini_pyramid[1,1]+mini_pyramid[2,2]
    
    a=np.zeros((3))
    
    a[0]=mini_pyramid[2,0]
    a[1]=mini_pyramid[2,1]
    a[2]=mini_pyramid[2,2]
    
    ans = (S,a)
    return ans

def make_endlist_for_comparator(i,j,list_S):
    A=np.zeros((i,j))
    for h in range(len(list_S)):
        for k in range(3):
            A[h,h+k]+=list_S[h][k]
    ans_list=np.amax(A,axis=0)
    return ans_list

def list_S_comparator(list_S,two_list):
    for i in range(len(list_S)):
        list_S[i]=list_S[i]+two_list[i]
    ans=make_endlist_for_comparator(len(list_S),len(list_S)+2,list_S)
    return ans

def make_mini_pyramid_3(x,y,f):
    '''
    makes a mini pyramid from the mega pyramid for analysis
    '''            
    l=np.zeros((3,3))
    
    l[0][0]=f[x][y]
    
    l[1][0]=f[x+1][y]
    l[1][1]=f[x+1][y+1]
    
    l[2][0]=f[x+2][y]
    l[2][1]=f[x+2][y+1]
    l[2][2]=f[x+2][y+2]
     
    return l


oldsum=0
two_list=[]
ans_list=[]
g_len=len(f)
for i in range(0,g_len-1,2):
    list_S=[]
    for j in range(i+1):
        mini_pyramid=make_mini_pyramid_3(i,j,f)
        S,B=initial_sum_list(mini_pyramid)
        S=S-B
        list_S.append(S)
    if(i==0):
        two_list=list_S[0]
    elif(i>0):
        length=len(list_S)
        ans_list=list_S_comparator(list_S,two_list)
        two_list=ans_list
print(ans_list)

for i in range(15):
    ans_list[i]=int(ans_list[i])+int(f[14][i])
print(ans_list)
print(max(ans_list))
        
    
        