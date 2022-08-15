#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    # Write your code here
    
    total_amt = 0
    not_consumed = bill[k]
    for i in bill:
        if i != not_consumed :
            total_amt = total_amt +i
        
    amt_to_be_paid = total_amt/2

    if b == amt_to_be_paid:
        print("Bon Appetit")
    else:
        print(int(b - amt_to_be_paid))



if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
