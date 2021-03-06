maze=[[1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [1,1,1,1]]
n=4  
def printsol(sol):
    for i in sol:
        for j in i:
            print(str(j)+" ",end="")
        print()
def issafe(maze,x,y):
    if 0<=x<n and 0<=y<n and maze[x][y]==1:
        return True
    return False
def solmaze(maze,x,y,sol):
    if x==n-1 and y==n-1 :
        sol[x][y]=1 
        return True
    if issafe(maze,x,y):
        sol[x][y]=1 
        if solmaze(maze,x+1,y,sol):
            return True
        if solmaze(maze,x,y+1,sol):
            return True  
        sol[x][y]=0
        return False
def solution(maze,n):
    sol=[[0 for j in range(4)]for i in range(4)]
    if not(solmaze(maze,0,0,sol)):
        print('solution doesnt exist')
        return False
    printsol(sol)
    return True
    
print(solution(maze,n))
