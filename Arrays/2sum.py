def twoSum(a,n,s) :
    a.sort() 
    i,j = 0,n-1 
    while i < j : 
        c = a[i] + a[j] 
        if c == s : 
            return True 
        elif c > s :
            j -= 1
        else : 
            i += 1
    return False

print(twoSum([1,-1,2,3],4,0))
