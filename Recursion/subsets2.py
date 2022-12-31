''' 
    Given an array of integers that may contain duplicates the task is to return all possible subsets. Return only unique subsets and they can be in any order.
'''
def solve(arr,i,curr,ans) : 
    if i == len(arr) : 
         dup = curr[::]
         dup = tuple(sorted(dup))
         ans.add(dup)
         return 
    
    curr.append(arr[i]) 
    solve(arr,i+1,curr,ans) 
    curr.pop() 
    solve(arr,i+1,curr,ans)

def uniqueSubsets(n,arr):
    ans = set()
    solve(arr,0,[],ans) 
    return ans

if __name__ == '__main__' : 
    n = 3 
    arr = [1,1,3] 
    ans = uniqueSubsets(n,arr) 
    for lis in ans : 
        print(*lis)
