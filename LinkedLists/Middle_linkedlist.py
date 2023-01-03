def findMiddle(head):
    fast,slow = head,head 
    while fast != None and fast.next != None :
        slow = slow.next
        fast = fast.next.next
    return slow