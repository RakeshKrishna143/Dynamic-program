def findMaxPath(a,row,col):
    for i in range(1,row):
        res=0
        for j in range(col):
            if j>0 and j<col-1:
                a[i][j]+=max(a[i-1][j],max(a[i-1][j-1],a[i-1][j+1]))
            elif j>0:
                a[i][j]+=max(a[i-1][j],a[i-1][j-1])
            elif j<col-1:
                a[i][j]+=max(a[i-1][j],a[i-1][j+1])
            res=max(a[i][j],res)
    return res
    
a= ([[ 10, 10, 2, 0, 20, 4 ], 
        [ 1, 0, 0, 30, 2, 5 ], 
        [ 0, 10, 4, 0, 2, 0 ], 
        [ 1, 0, 2, 20, 0, 4 ]]) 
                
print(findMaxPath(a,4,6)) 
