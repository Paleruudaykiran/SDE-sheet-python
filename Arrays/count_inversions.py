from sys import stdin
def merge(arr,lo,mid,hi) : 
    i = lo 
    j = mid + 1
    lis = [] 
    ct = 0
    while i <= mid and j <= hi : 
        if arr[i] <= arr[j] : 
            lis.append(arr[i]) 
            i += 1 
            
        else :
            lis.append(arr[j]) 
            j += 1
            ct = ct + (mid-i+1)   
    while i <= mid : 
        lis.append(arr[i]) 
        i += 1 
    while j <= hi : 
        lis.append(arr[j]) 
        j += 1
    k = 0 
    for i in range(lo,hi+1) :
        arr[i] = lis[k] 
        k += 1 
    return ct
def mergesort(arr,lo,hi) :
    ct = 0
    if lo < hi : 
        mid = lo + (hi - lo)//2
        ct += mergesort(arr,lo,mid) 
        ct += mergesort(arr,mid+1,hi) 
        ct += merge(arr,lo,mid,hi) 
    return ct
def getInversions(arr, n) :
    ct = mergesort(arr,0,n-1)
    return ct

# Taking inpit using fast I/O.
def takeInput() :
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

# Main.
arr, n = takeInput()
print(getInversions(arr, n))