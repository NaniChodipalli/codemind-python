x = input()
l = ['a','e','i','o','u']
m = ['A','E','I','O','U']
k=[]
for i in sorted(set(x),key=x.index):
    if (i in l) or (i in m):
        k.append(i)
print(*k)