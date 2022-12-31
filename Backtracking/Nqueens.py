def valid(i,j,n,curr) : 
    row = i 
    col = j 
    while row >= 0 and col >= 0 and col < n:
        if curr[row][col] == 1 : 
            return False 
        row -= 1 
    
    row,col = i,j 
    while row >= 0 and col < n :
        if curr[row][col] == 1 : 
            return False 
        row -= 1 
        col += 1
    
    row,col = i,j 
    while row >= 0 and col >= 0 : 
        if curr[row][col] == 1 : 
            return False 
        row -= 1 
        col -= 1
    
    return True

def generate(i,n,grid,ans) : 
    if i == n : 
        print(grid)
        return 
    curr = grid[:]
    for col in range(0,n) :
        if valid(i,col,n,curr) :
            curr[i][col] = 1 
            generate(i+1,n,curr,ans)
            curr[i][col] = 0 
           
def solveNQueens(n):
    grid = [[0 for j in range(n)] for i in range(n)] 
    ans = []
    generate(0,n,grid,ans)


if __name__ == '__main__' : 
    solveNQueens(4)