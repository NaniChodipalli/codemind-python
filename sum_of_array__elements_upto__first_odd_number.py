x = int(input())
l = list(map(int,input().split()))
c=0
for i in l:
    c+=i
    if i%2==1:
        d=i
        break
print(c-d)