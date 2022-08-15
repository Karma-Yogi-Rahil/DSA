#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def getMax(operations):
    maxnumber = 0 
    stack = []
    for i in operations:
        if str(i).startswith('1'):
            number = int((i[1:]).strip())
            if number >maxnumber:
                maxnumber = number
            stack.append(number)

        if str(i).startswith("2"):
            if len(stack)==1:
                maxnumber = 0
            stack.pop(-1)

        if str(i).startswith('3'):
            print(maxnumber)
            

            
    # Write your code here

if __name__ == '__main__':
   

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)
 


