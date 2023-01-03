def reverseLinkedList(head):
    prev = None 
    curr = head 
    far = head 
    while curr != None :
        far = curr.next 
        curr.next = prev 
        prev = curr 
        curr = far 
    return prev