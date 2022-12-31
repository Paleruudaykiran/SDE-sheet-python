# Dutch National Flag algorithm
def sort012(arr, n) :
    lo = 0 
    mid = 0 
    hi = n - 1 
    while mid <= hi :
        if arr[mid] == 0 :
            arr[lo],arr[mid] = arr[mid],arr[lo] 
            lo+= 1
            mid += 1 
        elif arr[mid] == 1 :
            mid += 1 
        elif arr[mid] == 2 : 
            arr[mid],arr[hi] = arr[hi],arr[mid] 
            hi -= 1 

arr = [0,1,0,2,0,1] 
sort012(arr,len(arr))
print(arr)