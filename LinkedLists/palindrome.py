def isPalindrome(head):
    stk = [] 
    curr = head
    while curr != None :
        stk.append(curr.data) 
        curr = curr.next 
    
    while head != None :
        if head.data != stk[-1] :
            return 0 
        stk.pop() 
        head = head.next
    return 1