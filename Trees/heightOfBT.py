def heightOfBT(root) :
    if root == None : 
        return 0
    
    lh = heightOfBT(root.left) 
    rh = heightOfBT(root.right) 
    
    return 1 + max(lh,rh)

heightOfBT(root)