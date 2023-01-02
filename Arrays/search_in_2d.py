def search(a,n,t) : 
    lo,hi = 0,n-1 
    while lo <= hi : 
        mid = lo + (hi - lo)//2 
        if a[mid] == t :
            return True 
        elif a[mid] < t : 
            lo = mid + 1 
        elif a[mid] > t :
            hi = mid - 1
    return False 

def binarySearch(mat,m,n,target):
    lo = 0
    hi = m*n - 1 
    while lo <= hi : 
        mid = lo + (hi - lo)//2 
        r,c = mid//n,mid%n 
        if mat[r][c] == target : 
            return True 
        elif mat[r][c] > target : 
            hi = mid - 1 
        elif mat[r][c] < target : 
            lo = mid + 1 
    return False
def findTargetInMatrix(mat, m, n, target):
    return binarySearch(mat,m,n,target)
    # for i in range(m):
    #     if mat[i][n-1] >= target :
    #         if search(mat[i],n,target) == True : 
    #             return True 
    # return False

mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12]] 
print(findTargetInMatrix(mat,3,4,10))
print(findTargetInMatrix(mat,3,4,13))