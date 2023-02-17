def constructBT(preo,ino,pst,ped,inst,ined,mp) :
    if pst > ped or inst > ined : 
        return None 
    root = Node(preo[pst]) 
    idx = mp[preo[pst]] 
    neles = idx - inst 
    
    root.left = constructBT(preo,ino,pst+ 1, pst + neles,inst, idx - 1, mp)
    root.right = constructBT(preo,ino,pst + neles+ 1, ped,idx + 1, ined, mp)
    
    return root
def buildTree(preorder,inorder) :
    mp = {} 
    for i in range(len(inorder)) :
        mp[inorder[i]] = i 
    preStart,inStart = 0,0 
    preEnd,inEnd = len(preorder)-1,len(inorder)-1 
    
    return constructBT(preorder,inorder,preStart,preEnd,inStart,inEnd,mp)
