def solve(arr,i,k,curr,ans) :
    if k == 0 and len(curr) != 0: 
        dup = curr[::]
        dup = tuple(dup)
        ans.add(dup)
    if i >= len(arr):
        return 
    curr.append(i) 
    solve(arr,i+1,k-arr[i],curr,ans) 
    curr.pop() 
    solve(arr,i+1,k,curr,ans)
def findSubsetsThatSumToK(arr, n, k) :
    ans = set()
    solve(arr,0,k,[],ans)
    res = [] 
    for lis in ans : 
        res.append([arr[i] for i in lis]) 
    return res
    
if __name__ == '__main__' : 
    n = 3 
    arr = [1,1,3] 
    k = 4
    ans = findSubsetsThatSumToK(arr,n,k) 
    for lis in ans : 
        print(*lis)
