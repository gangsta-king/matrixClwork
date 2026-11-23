n1,n2=map(int,input().split())
c=0
matrix=[[0]*n1 for i in range(n2)]
for i in range(n2):
    for j in range(n1):
        c+=1
        matrix[i][j]=c
print('Matrix:')
for i in range(n1):
    for j in range(n2):
       print(matrix[i][j],end=' ')
    print() 
print('Rows sum:')
print(*[sum(i) for i in matrix])