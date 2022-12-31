def ispalin(s) :
    return s == s[::-1]
def solve(s,i,curr,ans) :
    if i >= len(s) :
        ans.append(curr)
        return 
    for ind in range(i,len(s)) :
        if ispalin(s[i:ind+1]): 
            dup = curr[::]
            dup.append(s[i:ind+1]) 
            solve(s,ind+1,dup,ans)   
def partition(s):
    ans = [] 
    solve(s,0,[],ans)
    return ans

if __name__ == '__main__' : 
    s = "BaaB" 
    ans = partition(s) 
    print(ans)