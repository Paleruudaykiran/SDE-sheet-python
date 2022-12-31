def isValid(r,c,mat,ch) :
    for i in range(9) :
        if mat[i][c] == ch : 
            return False 
        
        if mat[r][i] == ch : 
            return False 
        
        if mat[3 * int(r / 3) + int(i / 3)][3 * int(c / 3) + i % 3] == ch : 
            return False 
    return True
                
def isItSudoku(matrix):
    for i in range(len(matrix)) : 
        for j in range(len(matrix[0])) : 
            if matrix[i][j] == 0 :
                for c in range(1,10) :
                    if isValid(i,j,matrix,c) :
                        matrix[i][j] = c 
                        if isItSudoku(matrix) :
                            return True
                        matrix[i][j] = 0
                return False                   
    return True