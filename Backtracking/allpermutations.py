def generate(i,n,lis) :
    if i == n : 
        print("".join(lis)) 
    curr = lis[::] 
    for j in range(i,n) :
        curr[i],curr[j] = curr[j],curr[i] 
        generate(i+1,n,curr) 
        curr[i],curr[j] = curr[j],curr[i] 
        
        
def findPermutations(s):
    s = list(s)
    n = len(s)
    generate(0,n,s)

if __name__ == '__main__' : 
    findPermutations("123")