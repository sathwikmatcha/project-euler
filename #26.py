

def recur_check(rem_list,f):
    ans=False
    for i in range(len(rem_list)-f):
        if(rem_list[i]==rem_list[i+f]):
            ans=True
    return ans

def update_addup(a,d,addup):
    
    ans2=-1
    
    while(True):
    
        if(a<d):
        
            ans2+=1
            a=a*10
            continue
        
        else:
            
            if(ans2==-1):
                ans2=0
            
            break
    
    return ans2
def term_check(rem_list):
    
    if(0 in rem_list):
        return True
    
    else:
        return False
    
def solve(a,d,rem_list,addup):
    
    ans1=0
    rem=basic_solve(a,d)
    
    if(rem==0):
        
        return ans1
    
    else:
        
        addup+=update_addup(rem,d,addup)
        rem_list.append(rem)
        
        '''recurrence check'''
        
        i=1
        
        while(i<len(rem_list)):
            
            if(recur_check(rem_list,i)):
        
                ans1=i
                break
            
            else:
                
                i+=1
                continue
        
        
        if(i==len(rem_list)):
            
            '''no recurrurence found'''
            return solve(rem,d,rem_list,addup)
        
        else:
            
            ans1+=addup
            return ans1
    
            
    

def basic_solve(a,d):
    
    while(True):
    
        if(a<d):
            a=10*a
            continue
        
        if(a>=d):
            a=a%d
            break
    
    return a 
            
            


N=1000;d=2
max_cnt=0;max_val=0


while(d<=N):
    rem_list=[]
    x=solve(1,d,rem_list,0)
    print("1/"+str(d)+"= "+str(1/d)+" ans= "+str(x))
    print("")
    if(x>max_cnt):
        max_cnt=x
        max_val=d
    
    d+=1
    
    
print(max_cnt)
print(max_val)
    
