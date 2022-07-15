x = int(input())
n = set(map(int,input().split()))
c=0
for i in list(n):
    if i%2==1:
        c+=i
print(c)
