# counting element that occurs more than n//2 times
def findMajorityElement(arr, n):
    for i in range(n):
        ct = 0
        for j in range(n): 
            if arr[i] == arr[j]: 
                ct += 1 
        if ct > n//2 : 
            return arr[i] 
    return -1

# moore voting algorithm
def findMajorityElement2(arr,n) :
    ct,ele = 0,-1 
    for i in range(n):
        if ct == 0 :
            ele = arr[i] 
        if arr[i] == ele :
            ct += 1
        else : 
            ct -= 1 
    return ele 