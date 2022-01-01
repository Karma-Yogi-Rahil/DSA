#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here
    
    no_div_list = []
    for i in range(len(s)):
        for j in range(i+1,len(s)) :
            #print(i,j)
            #print(s[i],s[j])
            if (s[i]+s[j]) % k != 0:
                #print(s[i],s[j])
                if s[i] not in no_div_list:
                    no_div_list.append(s[i])
                if s[j]not in no_div_list:
                    no_div_list.append(s[j])
    
    print(len(no_div_list))
        
    new_list = []
    for i in range(len(no_div_list)):
        for j in range(i+1,len(no_div_list)) :
            #print(i,j)
            #print(s[i],s[j])
            if (s[i]+s[j]) % 2 != 0:
                print(s[i],s[j])
                if s[i] not in new_list:
                    new_list.append(s[i])
                if s[j]not in new_list:
                    new_list.append(s[j])

    print(len(new_list))
            

            

    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    #fptr.write(str(result) + '\n')

    #fptr.close()
