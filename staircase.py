#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    i=0
    while i<n:
        j=1
        while j<=n:
            if j<n-i:
                print(" ", end="")
            else:
                print("#", end="")
            j+=1
        print("")
        i+=1

if __name__ == '__main__':
    n = int(input())

    staircase(n)
