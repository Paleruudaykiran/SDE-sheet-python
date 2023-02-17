from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque() 
        n = len(grid) 
        m = len(grid[0]) 

        for i in range(n) : 
            for j in range(m) : 
                if grid[i][j] == 2 : 
                    q.append((i,j,0)) 
        drow = [-1,1,0,0] 
        dcol = [0,0,1,-1]
        ans = 0
        while len(q) != 0 : 
            cell = q.popleft() 
            r,c,tm = cell 
            for i in range(len(drow)) : 
                nr = r + drow[i] 
                nc = c + dcol[i] 
                ntm = tm + 1 
                if nr >= 0 and nr < n and nc >= 0 and nc < m and grid[nr][nc] == 1 :
                    ans = ntm
                    grid[nr][nc] = 2
                    q.append((nr,nc,ntm)) 
        for i in range(n) : 
            for j in range(m) : 
                if grid[i][j] == 1 : 
                    return -1
        return ans

