def findIndex(arr,n,t) :
    l,r = 0,n-1
    ans = -1
    while l <= r :
        m = l + (r-l)//2 
        if arr[m] <= t :
            ans = m 
            l = m + 1
        else :
            r = m - 1
    return ans+1

def getMedian(matrix):
    n,m = len(matrix),len(matrix[0]) 
    l,r = 1,1e9 
    desired = (n*m+1)//2
    while l < r :
        mid = l + (r - l)//2 
        ct = 0
        for i in range(n) :
            ct += findIndex(matrix[i],m,mid)
        
        if ct < desired :
            l = mid + 1
        else :
            r = mid 
    return int(l)
        