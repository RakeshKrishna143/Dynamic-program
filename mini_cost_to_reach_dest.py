
INF=999999
cost=[ [0, 15, 80, 90],
    [INF, 0, 40, 50],
    [INF, INF, 0, 70],
    [INF, INF, INF, 0]]
    
def shortestpath(cost):
    res=-1
    for k in range(4):
        for j in range(4):
            if cost[0][j]>(cost[0][k]+cost[k][j]):
                cost[0][j]=(cost[0][k]+cost[k][j])
                res=k
                
                
    return cost[0],res+1
    
print(shortestpath(cost))
