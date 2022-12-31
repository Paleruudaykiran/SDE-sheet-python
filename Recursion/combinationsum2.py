def solve(arr,i,k,curr,ans,n) :
   
    if k == 0 and len(curr) != 0: 
        dup = curr[::]
        dup = tuple(dup)
        ans.add(dup)
    if i >= n or k < 0:
        return 
 
    curr.append(arr[i]) 
    solve(arr,i+1,k-arr[i],curr,ans,n) 
    curr.pop() 
    solve(arr,i+1,k,curr,ans,n)
def combinationSum2(arr, n, k):
    ans = set()
    arr.sort()
    solve(arr,0,k,[],ans,n)
    return sorted(list(ans))


if __name__ == '__main__' : 
    n = 3 
    arr = [1,1,3] 
    k = 4
    ans = combinationSum2(arr,n,k) 
    for lis in ans : 
        print(*lis)