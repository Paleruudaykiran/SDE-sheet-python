def maximumValue(items, n, w):
    items = sorted(items,key = lambda x : x[1]/x[0],reverse = True) 
    ans = 0
    i = 0
    while w != 0 and i < n:
        if items[i][0] <= w :
            ans += items[i][1] 
            w -= items[i][0]
            i += 1
        else :
            ans = ans + (w/items[i][0])*items[i][1] 
            w = 0
    return ans