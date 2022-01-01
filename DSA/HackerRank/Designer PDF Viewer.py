#!/bin/python3

import math
import os
import random
import re
import sys
import string

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    
    # Write your code here
    max_height = 0
    for i in range (len(word)):
        num = ord(word[i])-97
        if (h[num] >= max_height):
            max_height = h[num]
    area = len(word)*max_height
    print(area)


    """alphabets = list(string.ascii_lowercase)
    max_number = 0 
    for i in range(len(alphabets)):
        for j in word.lower():
            if alphabets[i] == j :
                
                value = h[i]
                
                if value > max_number :
                    max_number = value

    print(max_number*(len(word)))  """

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    #fptr.write(str(result) + '\n')

    #fptr.close()
