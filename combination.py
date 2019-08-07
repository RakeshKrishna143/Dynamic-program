target=3
a=['h','t']

def dfs(a,target,index,path,res):
    if len(path)==3:
        res.append(path)
        return 
    
    else:
        for i in range(index,len(a)):
            dfs(a,target-1,0,path+a[i],res)

def cs(a,target):
    res=[]
    dfs(a,target,0,'',res)
    return res 
print(cs(a,target))

