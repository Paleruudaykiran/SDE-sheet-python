def postorder(root) :
    if root != None :
        postorder(root.left) 
        postorder(root.right) 
        print(root.data,end=" ") 
    