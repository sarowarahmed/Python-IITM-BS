n = int(input())

identity_matrix = []

for i in range(n):
    row = [1 if j == i else 0 for j in range(n)]
    identity_matrix.append(row)

for row in identity_matrix:
    print(",".join(map(str, row)))
      
    

       



