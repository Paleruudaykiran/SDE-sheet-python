def removeDuplicates(arr,n):
    i,j = 0,1
    for j in range(n) :
        if arr[i] != arr[j] :
            i += 1
            arr[i] = arr[j] 
    return i+1