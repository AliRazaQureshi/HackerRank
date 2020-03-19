#!/bin/python3

import math
import os
import random
import re
import sys

def condition(n):
    if n % 2 == 0:
        if 2 <= n <= 5:
            print("Not Weird")

        elif 6 <= n <= 20:
            print("Weird")

        else:
            print("Not Weird")
        
    else:
        print("Weird")


if __name__ == '__main__':
    N = int(input())
    if 0 < N < 101:
        condition(N)
