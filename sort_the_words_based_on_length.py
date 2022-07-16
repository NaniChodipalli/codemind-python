l = list(map(str,input().split()))
s=0
m=[]
for i in l:
    for j in i:
        s+=ord(j)
    m.append([s,i])
    s=0
m.sort()
for i in m:
    print(i[1],end=" ")