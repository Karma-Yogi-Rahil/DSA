#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    # Write your code here
    b = []
    for i in range(0,len(a)-1):
        for j in range(len(a)-1,i,-1):
            #print(a[i],a[j])
            if a[i] == a[j] :
                #print(j-i)
                b.append((j-i)) 

    if len(b)!=0:
        print(min(b))
    else:
        print(-1)
    
    
                
    
                  
                
        

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

