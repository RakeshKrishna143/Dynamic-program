target=3
a=['h','t']

def dfs(a,target,index,path,res):
    if len(path)==target:
        res.append(path)
        return 
    
    else:
        for i in range(index,len(a)):
            dfs(a,target,0,path+a[i],res)
            #dfs(a,target,i,path+a[i],res)
            #dfs(a,target,i+1,path+a[i],res)


def cs(a,target):
    res=[]
    dfs(a,target,0,'',res)
    return res 
print(cs(a,target))

