maze=[[1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]]
 
def printsol(sol):
    path=[]
    for i in sol:
        for j in i:
            if j!=0:
                path.append(j)
    print(path)
def issafe(maze,x,y):
    if 0<=x<m and 0<=y<n:
        return True
    return False
def solmaze(maze,x,y,sol):
    if x==m-1 and y==n-1 :
        sol[x][y]=maze[x][y]
        return True
    if issafe(maze,x,y):
        sol[x][y]=maze[x][y]
        if solmaze(maze,x+1,y,sol):
            printsol(sol)
        if solmaze(maze,x,y+1,sol):
            printsol(sol)
        sol[x][y]=0
        
def solution(maze,m,n):
    sol=[[0 for j in range(4)]for i in range(4)]
    solmaze(maze,0,0,sol)
m=4 
n=4
solution(maze,m,n)
