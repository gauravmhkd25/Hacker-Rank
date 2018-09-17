st=input().split()
s = int(st[0])

t = int(st[1])

ab = input().split()

a = int(ab[0])

b = int(ab[1])

mn = input().split()

m = int(mn[0])

n = int(mn[1])

apples = list(map(int, input().rstrip().split()))

oranges = list(map(int, input().rstrip().split()))

app=[]
appl=0
appc=0
orrc=0
for val in apples:
    if s<=val+a<=t:
        appc+=1
appl=0
for val in oranges:
    if s<=val+b<=t:
        orrc+=1
        
print(appc)
print(orrc)

