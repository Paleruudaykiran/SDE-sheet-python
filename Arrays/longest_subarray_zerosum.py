def LongestSubsetWithZeroSum(arr):
    d = dict() 
    s,ans = 0,0 
    for i in range(len(arr)) :
        s += arr[i] 
        if s == 0 :
            ans = i + 1
        elif s in d.keys() :
            ans = max(ans,i-d[s]) 
        else :
            d[s] = i
    return ans