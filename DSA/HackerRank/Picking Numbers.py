#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a,n):
    # Write your code here
    a.sort()
    print(a)
    length = 0 
    start = 0
    num =1
    for i in range(n):
        print(a)
        print("i",i)
        print("len",length)
        print("start",start)
        print("num",num)
        print("----")
        
        if (a[i] - a[start]) >=2:
                num =1 
                length = max(length , i-start)
                start = i
        else :
            num+=1

    print(max(length,num))

if __name__ == '__main__':
 

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a,n)


