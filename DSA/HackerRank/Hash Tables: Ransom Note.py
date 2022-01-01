#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    # Write your code here
    magazine_dict = {}
    for i in magazine:
        if i in magazine_dict:
            magazine_dict[i]+=1
        else:
            magazine_dict[i]=1
    
    #print(magazine_dict)
    no_count = 0
    for j in note :
        if j in magazine_dict :
            
            if int(magazine_dict[j]) >0 :
                magazine_dict[j]-=1
               
            
            else:
                no_count=1
                
                break
        else :
            no_count=1
                
            break

    if no_count ==1:
        print('No')

    else:
        print('Yes')

      
    
    #print(magazine_dict)
        
            
    



        

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
