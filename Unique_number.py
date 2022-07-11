n=input()
c=0
for i in n:
    if n.count(i)==1:
        c+=1
if c==len(n):
    print("Unique Number")
else:
    print("Not Unique Number")