def rotate(head, k):
    if head == None or head.next == None or k == 0 :
        return head
    ct = 1 
    temp = head
    while temp.next != None :
        ct += 1
        temp = temp.next
    temp.next = head
    k = k%ct
    curr = head
    end = ct - k
    while end > 1 :
        curr = curr.next
        end -= 1
    head = curr.next
    curr.next = None
    return head