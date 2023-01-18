def uniqueSubstrings(s) :
    l,r = 0,0 
    lis = []
    ans = 1
    while r < len(s) :
        if s[r] not in lis :
            ans = max(ans,r-l+1) 
            lis.append(s[r])
            r += 1
        else :
            lis.remove(s[l]) 
            l += 1
    return ans