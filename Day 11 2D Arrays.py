#!/bin/python3

import math
import os
import random
import re
import sys

def sum_hourglass(a, i, j):
    Sum = a[i][j] + a[i][j + 1] + a[i][j + 2]
    i += 1
    Sum += a[i][j + 1]
    i += 1
    Sum += a[i][j] + a[i][j + 1] + a[i][j + 2]
    return Sum

def max_hourglass(a):
    Max = -9 * 100
    for i in range(0, 4):
        for j in range(0, 4):
            Sum = sum_hourglass(a, i, j)
            if Sum > Max:
                Max = Sum
    return Max

arr = []
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

print(max_hourglass(arr))