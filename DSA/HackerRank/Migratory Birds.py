#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    #print(arr)
    freq_dict = {}
    arr.sort()

    for item in arr :
        if item in freq_dict:
            freq_dict[item]+=1
        else :
            freq_dict[item]=1

    max_value = max(freq_dict, key=lambda key: freq_dict[key])
    print(max_value)
    

if __name__ == '__main__':
    

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

