#Morris inorder traversal
def mpreorder(root) :
    preorderlis = [] 
    curr = root 
    while curr != None :
        if curr.left == None :
            preorderlis.append(curr.data) 
            curr = curr.right 
        else :
            prev = curr.left 
            while prev.right != None or prev.right != curr :
                prev = prev.right 
            if prev.right == None :
                prev.right = curr 
                preorderlis.append(curr.data) 
                curr = curr.left 
            else :
                prev.right = None
                curr = curr.right 
    return preorderlis
    