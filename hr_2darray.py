m = int(input('number of rows, m = '))
mat=[]

for i in range(0,m):
    for j in range(0,m):
        #print('enter in row: ',i+1,'column: ',j+1)
        mat[i][j]=list(map(int,input().strip().split(' ')))
print(mat)
sum1=0
sum2=0
for i in range(0,m):
    for j in range(0,m):
        if i == j:
            print(mat[i][j])
            sum1+=mat[i][j]
mat.reverse()
for i in range(0,m):
    for j in range(0,m):
        if i == j:
            print(mat[i][j])
            sum2+=mat[i][j]
print(sum1,sum2)
