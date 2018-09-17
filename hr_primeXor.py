
x=int(input())
arr=list(map(int,input().strip().split(' ')))


def is_prime_number(arr):
    prime=True
    count=0
    com=0
    for val in arr:
        if 3500<=val<=4500:
            for i in range(2,val):
                   if val%i==0:
                       prime=False
                       break
                   else:
                       prime=True
                       break
            if prime==True or val==2:
                count+=1
            
    for val in arr:
        if 3500<=val<=4500:
            com^=val
    for i in range(2,com-1):
        if com%i==0:
            break
        else:
            count+=1
            break
    print(count)
            
is_prime_number(arr)
