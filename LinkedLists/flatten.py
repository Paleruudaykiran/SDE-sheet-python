def merge(l1,l2) :
    res = Node(-1) 
    temp = res 
    while l1 != None and l2 != None :
        if l1.data > l2.data :
            temp.child = l2 
            l2 = l2.child 
            temp = temp.child 
        else :
            temp.child = l1
            l1 = l1.child 
            temp = temp.child
    
    if l1 != None :
        temp.child = l1
    if l2 != None :
        temp.child = l2
    return res.child
            
    
def flatten(node) :
    if node == None or node.next == None:
        return node
    node.next = flatten(node.next) 
    node = merge(node,node.next) 
    return node
    
def flattenLinkedList(head):
    return flatten(head)