def generatePaths(r,c,n,maze,curr) : 
    if r == n-1 and c == n-1 :
        res = []
        for i in range(n) : 
            for j in range(n) : 
                res.append(curr[i][j]) 
        print(*res)
        return 
    drow = [1,-1,0,0] 
    dcol = [0,0,-1,1] 
    for i in range(4) : 
        nr = r + drow[i] 
        nc = c + dcol[i] 
        if nr >= 0 and nr < n and nc >= 0 and nc < n : 
            if maze[nr][nc] == 1 and curr[nr][nc] == 0:
                curr[nr][nc] = 1 
                generatePaths(nr,nc,n,maze,curr) 
                curr[nr][nc] = 0
def ratInAMaze(maze, n):
    curr = [[0 for i in range(n)] for j in range(n)]
    curr[0][0] = 1 
    generatePaths(0,0,n,maze,curr) 

if __name__ == '__main__' : 
    mat = [[1,0,1],[1,0,1],[1,1,1]] 
    ratInAMaze(mat,len(mat))