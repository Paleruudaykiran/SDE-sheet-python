def maxSubarraySum(arr, n) :
    msf = 0
    meh = 0
    start,end = -1,-1 
    s = 0
    for i in range(n) : 
        meh += arr[i] 
        if meh < 0 : 
            meh = 0 
            s = i + 1 
        if meh > msf : 
            msf = meh
            start,end = s,i
    
    for x in range(start,end+1) : 
        print(arr[x],end=" ")
    print()
    return msf

print(maxSubarraySum([1,2,-30,-2,23,3],6))