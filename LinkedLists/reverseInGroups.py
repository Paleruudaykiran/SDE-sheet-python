class Node:
    def __init__(self, data):
       	self.data = data
        self.next = None

def reverse(head,i,b) :
    if i == len(b) or head == None:
        return head
    ct = b[i] 
    if ct == 0 :
        return reverse(head,i+1,b)
    prev,far = None,head
    curr = head 
    while curr != None and ct != 0 :
        far = curr.next 
        curr.next = prev 
        prev = curr 
        curr = far 
        ct -= 1
    head.next = reverse(far,i+1,b) 
    
    return prev
    

def getListAfterReverseOperation(head, n, b):
    return reverse(head,0,b)