def lvgen(root,lis,level) :
    if root == None : 
        return 
    if len(lis) == level :
        lis.append(root.data) 
    
    if root.right : 
        lvgen(root.right,lis,level+1) 
    if root.left : 
        lvgen(root.left,lis,level+1) 
def leftView(root) :
    lis = [] 
    lvgen(root,lis,0) 
    return lis 