def rotateMatrix(mat):
    n = len(mat) 
    # Transpose matrix 
    for i in range(n) : 
        for j in range(n) :
            mat[i][j],mat[j][i] = mat[j][i],mat[i][j] 

    # Reverse each row 
    for i in range(n): 
        mat[i] = mat[i][::-1] 

    for row in mat : 
        print(*row) 

mat = [[1,2],[3,4]] 
rotateMatrix(mat)


