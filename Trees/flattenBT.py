from collections import deque
def flatten(root) :
    if root == None :
        return 
    stk = deque()
    stk.append(root)
    while len(stk) > 0 :
        node = stk.pop()
        
        if node.right :
            stk.append(node.right) 
        if node.left :
            stk.append(node.left) 
        
        if len(stk) > 0 :
            node.right = stk[-1] 
        node.left = None 