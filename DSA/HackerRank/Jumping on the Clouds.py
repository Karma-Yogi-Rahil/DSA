#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    result = 0 
    index = 0 
    while (index < len(c) - 1):
        if (index + 2 <= n - 1 and  c[index + 2] != 1):
            index = index + 2;
                
        else:
            index = index + 1;
                
        result+=1;
            
        
    print(result)

if __name__ == '__main__':
    

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

