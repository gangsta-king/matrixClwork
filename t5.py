n=int(input())
matrix=[[0]*n for i in range(n)]
for i in range(n):
    matrix[i][i]=1
    matrix[i][n-1-i]=1
    
for i in matrix:
    print(*i)