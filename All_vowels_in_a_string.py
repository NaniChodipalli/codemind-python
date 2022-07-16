x=input()
l = ['a','e','i','o','u']
m = ['A','E','I','O','U']   
k=[]
j=[]
for i in x:
    if i>='a' and i<='z':
        if i in l:
            k.append(i)
    else:
        if i in m:
            j.append(i)
k = set(k)
j = set(j)
if len(k)==5 or len(j)==5:
    print(True)
else:
    print(False)