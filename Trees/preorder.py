def preorder(root) : 
    if root == None : 
        return 
    print(root.data,end=" ") 
    preorder(root.left) 
    preorder(root.right) 
