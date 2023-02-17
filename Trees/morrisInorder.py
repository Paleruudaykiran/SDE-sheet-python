#Morris inorder traversal
def minorder(root) :
    inorderlis = [] 
    curr = root 
    while curr != None :
        if curr.left == None :
            inorderlis.append(curr.data) 
            curr = curr.right 
        else :
            prev = curr.left 
            while prev.right != None or prev.right != curr :
                prev = prev.right 
            if prev.right == None :
                prev.right = curr 
                curr = curr.left 
            else :
                prev.right = None 
                inorderlis.append(curr.data) 
                curr = curr.right 
    return inorderlis