import copy
def setZeroes(matrix):
    matrix2 = copy.deepcopy(matrix)
    for i in range(len(matrix2)):
        for j in range(len(matrix2[0])):
            if matrix2[i][j] == 0:
                for s in range(len(matrix[0])):
                    matrix[i][s] = 0
                for s in range(len(matrix)):
                    matrix[s][j] = 0
                    
    return matrix
print(setZeroes([[1,1,1],[1,0,1],[1,1,1]]))