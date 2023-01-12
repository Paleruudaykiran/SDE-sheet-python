
def count(firstHead) :
    ct = 0
    while firstHead != None :
        ct += 1
        firstHead = firstHead.next
    return ct
#     if firstHead == None :
#         return 0 
#     return 1 + count(firstHead.next) 

def findIntersection(firstHead, secondHead) :
    n1 = count(firstHead) 
    n2 = count(secondHead)
    dif = abs(n1-n2) 
    if n1 > n2 :
        while dif :
            firstHead = firstHead.next 
            dif -= 1
    if n2 > n1 :
        while dif : 
            secondHead = secondHead.next
            dif -= 1
    while True :
        if secondHead == firstHead :
            return firstHead.data
        secondHead = secondHead.next
        firstHead = firstHead.next 
        if firstHead == None or secondHead == None :
            return -1
  