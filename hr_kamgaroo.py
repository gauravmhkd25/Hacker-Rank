#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    a=[]
    b=[]
    a=[x1]
    b=[x2]
    for i in range(2,10):
        a[i]=a[i-1]+v1
        v1+=v1
    for i in range(2,10):
        b[i]=b[i-1]+v2
        v2+=v2
    for i in range(0,10):
        if a[i]==b[i]:
            result='Yes'
    return result


 

x1V1X2V2 = input().split()

x1 = int(x1V1X2V2[0])

v1 = int(x1V1X2V2[1])

x2 = int(x1V1X2V2[2])

v2 = int(x1V1X2V2[3])

result = kangaroo(x1, v1, x2, v2)

print(result)
