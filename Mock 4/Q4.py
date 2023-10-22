n = int(input())

matrix1 = []
for _ in range(n):
    row = list(map(int, input().split(',')))
    matrix1.append(row)
matrix2 = []
for _ in range(n):
    row = list(map(int, input().split(',')))
    matrix2.append(row) 
 
result_matrix = []
for i in range(n):
    new_row = [matrix1[i][j] + matrix2[i][j] for j in range(n)]
    result_matrix.append(new_row)
for row in result_matrix:
    print(','.join(map(str,row))) 