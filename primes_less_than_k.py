def prime(n):
    if n==1:
        return 0
    for i in range(2,(n//2)+1):
        if n%i==0:
            return 0
    return 1
x = int(input())
l = list(map(int,input().split()))
k = int(input())
b=0
for i in l:
    if prime(i):
        if i<=k:
            b+=1
print(b)