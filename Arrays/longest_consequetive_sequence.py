def lengthOfLongestConsecutiveSequence(arr, n):
    arr = list(set(arr))
    n = len(arr)
    arr.sort() 
    ans = 1
    prev = arr[0]
    curr = 1
    for i in range(1,n) :
        if arr[i] == prev + 1 or arr[i] == prev:
            curr += 1
        elif arr[i] != prev + 1 :
            curr = 1
        prev = arr[i]
        ans = max(ans,curr) 
    return ans