class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
      
def sortTwoLists(first, second):
    ans = Node(-1) 
    tail = ans
    if first == None :
        return second
    if second == None :
        return first 
    while first != None and second != None :
        if first.data >= second.data :
            tail.next = Node(second.data) 
            tail = tail.next
            second = second.next
        else :
            tail.next = Node(first.data) 
            tail = tail.next
            first = first.next
            
    if first :
        tail.next = first
    if second :
        tail.next = second
    return ans.next