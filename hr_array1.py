n=int(input())
arr=input()
score=list(map(int,arr.split(' ')))
count=len(score)
pc=0
nc=0
zc=0
for val in score:
    if val>0:
        pc+=1
    if val<0:
        nc+=1
    if val==0:
        zc+=1

fpc=pc/count
fnc=nc/count
fzc=zc/count

print(round(fpc,6))
print(round(fnc,6))
print(round(fzc,7))
