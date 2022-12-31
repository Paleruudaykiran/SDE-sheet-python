'''
     Given an array print all the sum of the subset generated from it, in the increasing order.
'''

def solve(nums,i,curr) :
    if i == len(nums) : 
        s = sum(curr) 
        return [s]
    curr.append(nums[i]) 
    lis1 = solve(nums,i+1,curr) 
    curr.pop() 
    lis2 = solve(nums,i+1,curr) 
    return lis1 + lis2
def subsetSum(nums):
    ans = solve(nums,0,[]) 
    ans.sort()
    return ans

if __name__ == '__main__' : 
    ans = subsetSum([1,2,3]) 
    print(ans)