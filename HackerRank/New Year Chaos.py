#!/bin/python3

import math
import os
import random
import re
import sys
from typing import final

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

t =int(input())
initial_list_legth  = int(input())

initial_list = list(map(int, input().rstrip().split()))

final_list_legth  = int(input())

final_list = list(map(int, input().rstrip().split()))
no_of_bribe = 0 

for I in range(1, n + 1): # for each person I in the list
    index = q.index(I)
    if I - index > 3: # more than two bribes
        bribes = "Too chaotic"
        break
    for j in range(index): # for each number to the left of I, if greater than I, count it as a bribe
        if q[j] > I: 
            bribes = bribes + 1
print bribes

