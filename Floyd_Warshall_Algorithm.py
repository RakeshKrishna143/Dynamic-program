#Floyd Warshall Algorithm
INF  = 99999
graph = [[0,5,INF,10], 
             [INF,0,3,INF], 
             [INF, INF, 0,   1], 
             [INF, INF, INF, 0] 
        ] 
print(graph)
def algorithm(graph):
    for k in range(4):
        for i in range(4):
            for j in range(4):
                graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
    return graph
    
algorithm(graph)
print(graph)
