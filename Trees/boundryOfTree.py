def leaves(root,res) :
    if root == None :
        return 
    if root.left == None and root.right == None :
        res.append(root.data) 
        return 
    leaves(root.left,res)
    leaves(root.right,res) 
        
def rightboundary(root) :
    if root == None :
        return []
    if root.left == None and root.right == None :
        return []
    curr,ls,rs = [root.data],[],[] 
    if root.right :
        ls = rightboundary(root.right) 
    else :
        rs = rightboundary(root.left) 
    return ls + rs + curr
def leftboundary(root,res) :
    if root == None :
        return 
    if root.left == None and root.right == None :
        return 
    res.append(root.data) 
    if root.left :
        leftboundary(root.left,res) 
    else :
        leftboundary(root.right,res) 
        
def boundary(root) :
    res = [] 
    leftboundary(root,res)
    leaves(root,res) 
    rev = rightboundary(root.right) 
    return res + rev[::-1]