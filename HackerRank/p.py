
from typing import Counter


c = [0,0,0,0,1,0]
count = 0
ans = 0
n =len(c)

while count < n-1 :
    count +=(c([count+2]==0)+1)
    ans +=1


print(count)

