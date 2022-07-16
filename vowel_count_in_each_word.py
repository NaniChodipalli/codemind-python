x = list(map(str,input().split()))
l = ['a','e','i','o','u']
m = ['A','E','I','O','U']  
for i in x:
    s=0
    for j in i:
        if (j in l) or (j in m):
            s+=1
    print(s,end=" ")