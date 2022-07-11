n,m=map(int,input().split())
c=max(n,m)
while True:
    if c%n==0 and c%m==0:
        print(c)
        break
    c+=1