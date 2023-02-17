def checksy(n1,n2) :
    if n1 == None and n2 == None : 
        return True 
    if n1 == None or n2 == None :
        return False 
    
    return (n1.data == n2.data
            and checksy(n1.left,n2.right) 
            and checksy(n1.right,n2.left))

def isSymetric(root) : 
    return checksy(root.left,root.right)
