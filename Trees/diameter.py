def diameter(root) :
    lis = [0]
    height(root,lis) 
    return lis[0]

def height(root,diameter) :
    if root == None :
        return 0 
    
    lh = height(root.left,diameter) 
    rh = height(root.left,diameter) 
    
    diameter[0] = max(lh+rh,diameter[0])
    
    return 1 + max(lh,rh)

diameter(root)