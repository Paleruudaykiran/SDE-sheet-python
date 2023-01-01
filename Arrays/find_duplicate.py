def findDuplicate(arr, n):
    i = 0 
    while i < n: 
        if arr[i] != i + 1 and arr[i] != arr[arr[i]-1]: 
            tp = arr[i] 
            arr[i] = arr[arr[i]-1]
            arr[tp-1] = tp
        else : 
            i += 1 
    print(arr)
    for i in range(n) : 
        if arr[i] != i + 1 : 
            return arr[i]

print(findDuplicate([1,4,2,1,3],5))