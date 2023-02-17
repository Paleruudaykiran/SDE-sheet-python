def identical(n1,n2) :
    if n1 == None and n2 == None :
        return True 
    elif n1 == None or n2 == None :
        return False 
    
    return (n1.data == n2.data
           and identical(n1.left,n2.left)
           and identical(n1.right,n2.right)) 
