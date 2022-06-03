n=int(input())
sum1=0
sum2=0
sum3=0
while n>0:
    r=n%10
    n=n//10
    sum1=sum1+r
while sum1>0:
    r1=sum1%10
    sum1=sum1//10
    sum2=sum2+r1
while sum2>0:
    r2=sum2%10
    sum2=sum2//10
    sum3=sum3+r2
print(sum3)
    
