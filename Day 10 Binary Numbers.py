#!/bin/python3

def decimalToBinary(dec):
    binary = bin(dec)
    binary = binary[2:]
    max_len = 0
    count = 0
    for bit in binary:
        if int(bit):
            count += 1
        else:
            count = 0
        if count > max_len:
            max_len = count
    print(max_len)

if __name__ == '__main__':
    n = int(input())
    decimalToBinary(n)