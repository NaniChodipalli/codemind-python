x = input()
y = input()
c=1
for i in range(len(x)):
    if x[i]==y:
        print(True)
        print(i)
        c=0
        break
if c==1:
    print(False)