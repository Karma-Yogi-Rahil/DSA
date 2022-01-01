#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write your code here

    count_same = 0
    ans = 0  
    if t in s :
        ans = len(t)

        if ans < k:
            print('Yes')

        else :
            print("No")
        
        
    else:
        for i in range (len(s)):
            if i <= len(t)-1:
                if s[i] == t[i]:
                    count_same+=1

        ans = len(s[count_same-1:]) + len(t[count_same-1:])

        if ans > k:
            print('No')

        


        

        else :

            if ans <= k-2:
                print('No')
            else:
                print("Yes")

    

    
    

    
    


if __name__ == '__main__':
   

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

