#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    if abs(z-x) > abs(z-y):
        print('Cat B')

    elif abs(z-x) == abs(z-y) :
        print('Mouse C')

    else :
        print("Cat A")

if __name__ == '__main__':
    

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)


