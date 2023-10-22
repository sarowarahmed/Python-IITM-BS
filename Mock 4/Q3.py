n = int(input())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
    
s = int(input())
result_matrix = [[element * s for element in row] for row in matrix]

for row in result_matrix:
    print(" ".join(map(str, row)))
