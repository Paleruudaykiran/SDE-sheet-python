# Extended Moore's voting algorithm
def findMajorityElement(a, n):
    c1,c2,n1,n2= 0,0,-1,-1
    for i in range(n) :
        if a[i] == n1 :
            c1 +=1 
        elif a[i] == n2:
            c2 += 1
        elif c1 == 0:
            n1 = a[i] 
            c1 = 1
        elif c2 == 0:
            n2 = a[i] 
            c2 = 1
        else :
            c1 -= 1
            c2 -= 1
    return [n1,n2]
