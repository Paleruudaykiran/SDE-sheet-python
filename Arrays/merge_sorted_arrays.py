import math
# merging arrays without extra space
# gap method 
# gap = (m + n) / 2  (ceil value) 

def merge(arr1,arr2,n,m) : 
    gap  = int(math.ceil((m+n)/2)) 
    while gap > 0 : 
        i,j = 0,gap
        while j < n + m : 
            if j < n : 
                if arr1[i] > arr1[j] : 
                    arr1[i],arr1[j] = arr1[j],arr1[i] 
            elif j >= n and i < n: 
                if arr1[i] > arr2[j-n] : 
                    arr1[i],arr2[j-n] = arr2[j-n],arr1[i] 
            elif j >= n and i >= n : 
                if arr2[i-n] > arr2[j-n] : 
                    arr2[i-n],arr2[j-n] = arr2[j-n],arr2[i-n]
            i += 1 
            j += 1
        if gap == 1 : 
            gap = 0 
        else : 
            gap = int(math.ceil(gap/2)) 
        
    print(arr1,arr2) 

merge([1,5,10,15],[2,3,4],4,3)




