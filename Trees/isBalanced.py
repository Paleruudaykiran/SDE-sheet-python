def isBalanced(root) :
    if check(root)!= -1 :
        return True 
    return False 

def check(root) :
    if root == None : 
        return 0 
    
    lh = check(root.left) 
    if lh == -1 :
        return -1 
    
    rh = check(root.right) 
    if rh == -1 : 
        return -1 
    
    if(abs(lh-rh) > 1) : 
        return -1 
    
    return 1 + max(lh,rh) 
