#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    # Write your code here
    arr.sort()

    i = 0
    while len(arr)!=0:
        print(len(arr))
        small_stick = min(arr)
        arr = [i-small_stick for i in arr]
        
        arr =[ i for i in arr if i!=0]
        


    

        
        
        #print(count)
                
            

if __name__ == '__main__':
    

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

