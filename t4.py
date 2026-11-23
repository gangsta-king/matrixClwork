n2,n1=map(int,input().split())
c=0
matrix=[[0]*n1 for i in range(n2)]
for i in range(n2):
    for j in range(n1):
        c+=1
        matrix[i][j]=c
print('Array:')
for i in matrix:
    for j in i:
        print(j,end=' ')
    print()
print('Transposed Matrix: ')
for i in range(n1):
    for j in range(n2):
       print(matrix[j][i],end=' ')
    print() 