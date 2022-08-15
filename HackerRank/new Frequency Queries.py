#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    freq_dict = {}
    
    ans = []
    for i in range(len(queries)):
        
        #print(queries[i][1])
        
        if queries[i][0] == 1:
            if queries[i][1] in freq_dict:
                freq_dict[queries[i][1]]+=1
            else :
                freq_dict[queries[i][1]]=1
            

        elif queries[i][0] == 2:
            if queries[i][1] in freq_dict:
                freq_dict[queries[i][1]]-=1

        

        elif queries[i][0] == 3:
            if  queries[i][1] in freq_dict.values():
                print('1')
                    
            else:
                print('0')
                    
                

                
   
                    
                
                    

                
        

            


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)


