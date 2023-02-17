class Solution:
    def dfs(self,i,adjlis,vis) :
        vis[i] = 1 
        for node in adjlis[i] :
            if vis[node] == 0 :
                self.dfs(node,adjlis,vis) 
        
                

    def findCircleNum(self, isConnected) -> int:
        n = len(isConnected) 
        vis = [0 for i in range(n)] 
        ct = 0
        adjlis = [[] for i in range(n)] 
        for i in range(n) :
            for j in range(n) :
                if isConnected[i][j] == 1 and i!=j :
                    adjlis[i].append(j) 
                    adjlis[j].append(i)
        for i in range(n) :
            if vis[i] == 0 :
                self.dfs(i,adjlis,vis)
                ct += 1
        return ct