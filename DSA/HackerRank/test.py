r=int(input())
c=int(input())
sum=0
m=0
id=0
for i in range(r):
    for j in range(c):
        sum+=int(input())
    if sum>m:
        m=sum
        id=i+1
    sum=0
print(id)