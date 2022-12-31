# brute force - using recursion 
# TC -> O(n!)
def generate(i,n,curr,res) :
    if i > n : 
        return 
    if i == n : 
        res.append(curr)
    ncurr = curr[:] 
    for j in range(i,n) : 
        ncurr[i],ncurr[j] = ncurr[j],ncurr[i] 
        generate(i+1,n,ncurr,res) 
        ncurr[i],ncurr[j] = ncurr[j],ncurr[i] 
def kthPermutationRec(n, k):
    lis = [str(i) for i in range(1,n+1)] 
    p = []
    generate(0,n,lis,p) 
    p.sort() 
    return "".join(p[k-1])

# optimized by using maths
def kthPermutation(n, k):
    nums = [] 
    fact = 1
    for i in range(1,n) : 
        nums.append(i) 
        fact = fact * i 
    nums.append(n)
    k -= 1 
    ans = ""
    while True : 
        ans = ans + str(nums[int(k//fact)]) 
        nums.remove(nums[int(k//fact)]) 
        if len(nums) == 0 : 
            break 
        k = k % fact 
        fact = fact / len(nums) 
    return ans

if __name__ == '__main__' : 
    ans = kthPermutation(3,2)
    print(ans)