#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    if len(a)==0:
        return a
    d=d % len(a)
    a=(a[d:] + a[:d])
    for val in a:
        print(val, end=' ')

nd = input().split()

n = int(nd[0])

d = int(nd[1])

a = list(map(int, input().rstrip().split()))

rotLeft(a, d)


    
