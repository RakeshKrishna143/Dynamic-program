maze = [[0, 0, 0, 0], 
		[0, -1, 0, 0], 
		[-1, 0, 0, 0], 
		[0, 0, 0, 0 ]] 
def count(maze,n):
    #activate row wise first col
    for i in range(n):
        if maze[i][0]==0:
            maze[i][0]=1 
        else:
            break
    #activate colwise first row
    for i in range(1,n):
        if maze[0][i]==0:
            maze[0][i]=1 
        else:
            break
    #expect first row and col
    for i in range(1,4):
        for j in range(1,4):
            if maze[i][j]==-1:
                continue
            #preious row
            if maze[i-1][j]>0:
                maze[i][j]+=maze[i-1][j]
            #previous col
            if maze[i][j-1]>0:
                maze[i][j]+=maze[i][j-1]
    print(maze[n-1][n-1])
count(maze,4)
