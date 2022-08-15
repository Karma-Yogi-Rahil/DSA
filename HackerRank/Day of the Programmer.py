#!/bin/python3

import math
import os
import random
import re
import sys
from typing import DefaultDict

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here
        if year == 1918:
            print('26.09.1918')
        elif ((year <= 1917) & (year % 4 == 0)) or ((year % 400 == 0) or ((year % 4 == 0) & (year % 100 != 0))):
            print('12.09.%s' %year)
        else:
            print('13.09.%s' %year)

    
"""days = 243
    if year > 1918:

        if year % 4 ==0 and year %100 !=0 or year%400==0:
            days +=1
        else:
            days = days
    
    elif year == 1918:
        print('26.09.1918')
    else:
        if year%4 == 0 :
            days+=1
        else:
            day =days

    day = 256-days
    print(f"{day}.09.{year}")"""

        

if __name__ == '__main__':


    year = int(input().strip())

    result = dayOfProgrammer(year)


