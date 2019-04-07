#!/bin/python3

import os

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    i = 0
    height = 1
    while i<n:
        i = i + 1
        if i%2==0:
            height +=1
        else:
            height = 2*height
            
    return height

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        print(str(result))

