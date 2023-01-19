def findTriplets(arr, n, target):
    arr.sort()
    ans = []
    #print(arr)
    for i in range(n) :
        if i == 0 or arr[i] != arr[i-1] :
            j = i + 1
            k = n - 1
            tar = target - arr[i]
            while j < k :
                s = arr[j] + arr[k] 
                #print("s tar",s,tar,i,j,k)
                if s == tar:
                    triplet = [arr[i],arr[j],arr[k]]
                    #print('triplet',triplet)
                    ans.append(triplet)
                    j += 1
                    k -= 1
                    while j < k and arr[j] == arr[j-1] :
                        j += 1
                    while j < k and arr[k] == arr[k-1] :
                        k -= 1
                elif s > tar :
                    k -= 1
                elif s < tar :
                    j += 1
    
    return ans