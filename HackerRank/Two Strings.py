#!/bin/python3

import math
import os
import random
import re
import sys
from typing import Dict

#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def twoStrings(s1, s2):
    # Write your code here
  
    s1_dict = {}
    for i in s1 :
        if i in s1_dict:
            s1_dict[i]+=1
        else:
            s1_dict[i]=1

    
    a=''        
    for j in s2:
        if j in s1_dict:
            a='Yes'
            break
    
    if a == 'Yes':
        print('YES')
    else:
        print('NO')
        
    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)


