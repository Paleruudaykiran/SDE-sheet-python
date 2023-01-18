def subarraysXor(arr, x):
    d = {} 
    cpx,c = 0,0 
    for i in range(len(arr)) :
        cpx ^= arr[i]
        if cpx == x :
            c+=1
        h = cpx^x
        if h in d.keys() :
            c = c + d[h] 
        if cpx in d.keys():
            d[cpx] += 1
        else :
            d[cpx] = 1
    return c