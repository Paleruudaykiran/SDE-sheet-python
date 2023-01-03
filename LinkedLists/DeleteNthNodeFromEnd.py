class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

def removeKthNode(head, k):
    if head is None or k == 0:
        return head

    slow = head
    fast = head

    for i in range(k):

        # If head is the Kth node from end of Linked List.
        if (fast.next == None):
            next = head.next
            head.next = None
            head = next

            return head
        else:
            fast = fast.next

    # Moving both slow and fast pointer with same speed.
    while (fast.next != None):
        slow = slow.next
        fast = fast.next

    # Removing the Kth node from end of Linked List.
    slow.next = slow.next.next

    return head

def build_linkedList(arr):
    head = None
    for i in range(len(arr)):
        if arr[i] == -1:
            break

        new = Node(arr[i])

        if head is None:
            head = new
            tail = new

        else:
            tail.next = new
            tail = tail.next

    return head

# Main Code
t = int(input().strip())
for i in range(t):
    k = int(input().strip())
    arr = [int(i) for i in input().strip().split()]

    head = build_linkedList(arr)
    res_head = removeKthNode(head, k)

    while res_head is not None:
        print(res_head.data, end= " ")
        res_head = res_head.next
    print(-1)
