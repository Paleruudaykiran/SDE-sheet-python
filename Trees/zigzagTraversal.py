from collections import deque
def zigzagt(root) :
    lis = [] 
    if root == None :
        return [] 
    q = deque() 
    q.append(root) 
    ltor = True
    while(len(q)>0) :
        size = len(q)
        row = [0 for i in range(size)]
        
        for i in range(size) :
            front = q.popleft() 
            
            if ltor :
                index = i 
            else :
                index = size - i - 1 
                
            
            row[index] = front.data 
            
            if front.left :
                q.append(front.left) 
            if front.right : 
                q.append(front.right) 
        lis.append(row) 
        ltor = True if ltor == False else False
    return lis