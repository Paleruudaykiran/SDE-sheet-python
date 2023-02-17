def convertcsp(root) :
    if root == None : 
        return 
    
    child = 0 
    if root.left : 
        child += root.left.data 
    if root.right : 
        child += root.right.data 
    
    if child < root.data :
        if root.left : 
            root.left.data = root.data 
        elif root.right :
            root.right.data = root.data 
    
    convertcsp(root.left) 
    convertcsp(root.right) 
    
    tot = 0
    if root.left : 
        tot += root.left.data 
    if root.right : 
        tot += root.right.data 
    
    if root.left or root.right :
        root.data = tot 
