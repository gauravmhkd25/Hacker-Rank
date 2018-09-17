n=5
arr=input()
num=list(map(int,arr.strip().split(' ')))

num.sort(reverse=False)

sum1=0
for i in range(0,4):
    sum1+=num[i]

sum2=0
for i in range(4,0,-1):
    sum2+=num[i]
print(sum1,sum2)

