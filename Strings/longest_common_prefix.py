def longestCommonPrefix(arr, n):
    arr.sort() 
    s = ""
    for i in range(len(arr[0])) :
        if arr[0][i] == arr[-1][i] :
            s += arr[0][i] 
        else :
            break 
    return s