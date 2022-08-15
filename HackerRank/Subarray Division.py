#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    #print(s,d,m)

    # Write your code here
    count = 0
    # Assuiming only one element in the list 
    if len(s) == 1:
            if s[0] == d:
                count +=1 
    
    # for more than six element 
    for i in range(len(s)-1):
        
        #print(sum(s[i:i+m]),d)
        if sum(s[i:m+i]) == d:
            count+=1

    print(count)
        
    


if __name__ == '__main__':
    

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)


