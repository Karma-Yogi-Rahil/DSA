#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    stack = []
    for charater in s :
        if charater in ['{','[','(']:
            stack.append(charater)

        else :
            if not stack:
                return False
            poped_charater = stack.pop()
            if poped_charater == '{':
                if charater != '}':
                    return False
            
            if poped_charater == '[':
                if charater != ']':
                    return False

            if poped_charater == '(':
                if charater != ')':
                    return False 

    if stack:
        return False
    return 'hi'


if __name__ == '__main__':
    

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        

    
