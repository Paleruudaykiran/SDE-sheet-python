def rvgen(root,lis,level) :
    if root == None :
        return 
    if len(lis) == level : 
        lis.append(root.data) 
    
    if root.left : 
        rvgen(root.left,lis,level+1) 
    if root.right :
        rvgen(root.right,lis,level+1) 
def rightView(root) :
    lis = [] 
    rvgen(root,lis,0) 
    return lis