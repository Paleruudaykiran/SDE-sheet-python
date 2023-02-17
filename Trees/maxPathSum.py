import sys
def maxPathSum(root) :
    lis = [-sys.maxsize]
    findMaxPathSum(root,lis) 
    return lis[0] 

def findMaxPathSum(root,maxi) :
    if root == None :
        return 0 
    
    lmax = max(0,findMaxPathSum(root.left,maxi))
    rmax = max(0,findMaxPathSum(root.right,maxi))
    
    maxi[0] = max(maxi[0],lmax+rmax+root.data) 
    
    return max(lmax,rmax) + root.data