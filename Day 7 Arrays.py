#!/bin/python3

import math
import os
import random
import re
import sys

def rev_array(arr):
    for index in reversed(range(0, len(arr))):
        print(arr[index], end = " ")

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    rev_array(arr)
