x = list(map(str, input().split()))
l = []
y = 'aeiouAEIOU'
for i in x:
    for j in i:
        if j not in y:
            l.append(j)
    l.sort()
    k = 0
    for j in i:
        if j in y:
            print(j, end="")
        else:
            print(l[k], end="")
            k += 1
    print(end=" ")
    l.clear()