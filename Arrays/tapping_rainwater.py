def getTrappedWater(arr, n) :
    leftMax = [arr[0]]
    rightMax = [arr[n-1]]
    for i in range(1,n) :
        leftMax.append(max(leftMax[-1],arr[i])) 
    for i in range(n-2,-1,-1) :
        rightMax.append(max(rightMax[-1],arr[i])) 
    rightMax = rightMax[::-1] 
    ct = 0
    for i in range(1,n-1) :
        ct += (min(rightMax[i],leftMax[i]) - arr[i])
    return ct

# without extra-space
def getTrappedWater2(arr, n) :
    leftMax = arr[0]
    rightMax = arr[n-1] 
    l,r = 0,n-1
    ct = 0
    while l < r :
        if arr[l] <= arr[r] :
            if arr[l] > leftMax :
                leftMax = arr[l] 
            else :
                ct += (leftMax - arr[l]) 
            l += 1
        else :
            if arr[r] > rightMax :
                rightMax = arr[r] 
            else :
                ct += (rightMax-arr[r]) 
            r -= 1
    return ct