def firstNode(head):
    f = head
    s = head 
    while f != None and f.next != None :
        f = f.next.next
        s = s.next
        if f == s :
            extra = head
            ct = 0
            while True:
                if extra == s :
                    return s
                extra = extra.next
                s = s.next
                ct += 1
    return -1