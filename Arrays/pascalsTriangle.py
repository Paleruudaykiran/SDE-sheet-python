def printPascal(n):
    lis = [[1]] 
    for i in range(n-1) : 
        prev = lis[-1] 
        nprev = len(prev) 
        curr = [1]
        for j in range(nprev-1) : 
            curr.append(prev[j+1]+prev[j])
        curr.append(1) 
        lis.append(curr) 
    for l in lis : 
        print(*l)

printPascal(5)