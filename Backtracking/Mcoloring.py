def isSafe(node,clr,clrs,n,mat) : 
    for i in range(n) : 
        if mat[i][node] == 1 :
            if clrs[i] == clr and i != node: 
                return False 
    return True 
def colorGraph(node,clrs,m,n,mat) :
    if node == n : 
        return True 
    for i in range(1,m+1) :
        if isSafe(node,i,clrs,n,mat) :
            clrs[node] = i 
            if colorGraph(node+1,clrs,m,n,mat) :
                return True 
            clrs[node] = -1 
    return False
def graphColoring(mat,m):
    n = len(mat) 
    clrs = [-1 for i in range(n)] 
    if colorGraph(0,clrs,m,n,mat) :
        return "YES" 
    else : 
        return "NO"

if __name__ == '__main__' : 
    mat = [[0,1,0],[1,0,1],[0,1,0]] 
    print(graphColoring(mat,1))
    print(graphColoring(mat,2))