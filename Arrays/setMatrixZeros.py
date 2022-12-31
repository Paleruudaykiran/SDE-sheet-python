def setZeros(matrix):
    n = len(matrix)
    m = len(matrix[0]) 
    row = [0 for i in range(m)] 
    col = [0 for i in range(n)]
    for i in range(n) :
        for j in range(m) :
            if matrix[i][j] == 0 :
                row[j] = 1
                col[i] = 1
    for i in range(n) :
        for j in range(m) :
            if row[j] == 1 or col[i] == 1:
                matrix[i][j] = 0

matrix = [[1,2,1],[0,3,4]]
setZeros(matrix) 
print(matrix)