def detectCycle(head) :
    s = head
    f = head 
    while f!=None and f.next != None :
        s = s.next
        f = f.next.next
        if s == f :
            return 1
    return 0
        