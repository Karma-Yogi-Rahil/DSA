#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):

    #
    # Write your code here.
  

    #
    max_money = 0

    for i in keyboards:
        for j in drives:
            
            if i+j > max_money and i+j <= b:
                max_money = i+j

            
    if max_money == 0 :
        print(-1)
    else:

        print(max_money)

if __name__ == '__main__':
   

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

