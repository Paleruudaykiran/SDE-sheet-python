def calculateMinPatforms(at, dt, n):
    at.sort()
    dt.sort()
    platforms,res = 1,1
    i,j = 1,0
    while i < n and j < n :
        if at[i] <= dt[j] :
            platforms += 1
            i += 1
        else :
            platforms -= 1
            j += 1
        res = max(platforms,res) 
    return res