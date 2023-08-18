def transpose(matrix):
    answer_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            answer_matrix[i][j] = matrix[j][i]
    return answer_matrix

print(transpose([[1,2,3],[4,5,6],[7,8,9]]))