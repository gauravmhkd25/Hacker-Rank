import numpy as np
m=int(input())
arr=list(map(int,input().strip().split(' ')))

arr2=list(map(int,input().strip().split(' ')))

arr3=list(map(int,input().strip().split(' ')))

data=np.transpose([arr,arr2,arr3])
#print(data)

sum1=0
sum2=0

for i in range(0,m):
    for j in range(0,m):
        if i==j:
            sum1+=data[i][j]
            #print(data[i][j])
rev=np.fliplr(data)
#print(rev)
for i in range(0,m):
    for j in range(0,m):
        if i==j:
            sum2+=rev[i][j]
            #print(rev[i][j])
print(abs(sum1-sum2))
