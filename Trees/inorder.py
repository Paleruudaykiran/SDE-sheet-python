def inorder(root) : 
    if root == None : 
        return 
    inorder(root.left) 
    print(root.data,end=" ") 
    inorder(root.right) 
