#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter 
#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    # Write your code here
    print(len(s))
    s = Counter(s)
    max_vale = max(s.values())
    print(max_vale)
    min
    
    print(s)


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

