def nextPermutation(permutation, n):
    #find the right most index whose value is less that its next element 
    ind = -1
    for i in range(n-2,-1,-1) : 
        if permutation[i] < permutation[i+1] : 
            ind = i 
            break
    if ind == -1 : 
        return permutation[::-1] 
    
    # find the right most element whose value is greater than value at ind 
    for i in range(n-1,-1,-1) : 
        if permutation[i] > permutation[ind] : 
            ind2 = i  
            break
    permutation[ind],permutation[ind2] = permutation[ind2],permutation[ind] 
    permutation = permutation[:ind+1] + permutation[ind+1:][::-1] 
    
    return permutation

print(nextPermutation([2,1,3],3))