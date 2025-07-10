#!/bin/python3
# time exceeded
import math
import os
import random
import re
import sys

def sum_of_multiples(n,k):
    num_of_multiples = (n-1)//k
    return int(k*num_of_multiples*(num_of_multiples+1)//2)
def sum_of_multiples2(n,k):
    num_of_multiples = (n-1)//k
    return int(k*num_of_multiples*(num_of_multiples+1)/2)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        print(sum_of_multiples(n,3) + sum_of_multiples(n,5) - sum_of_multiples(n,15))


    # # for i in range(1,10**9):/
    # i = 265593093
    # a = sum_of_multiples(i,3) + sum_of_multiples(i,5) - sum_of_multiples(i,15)
    # b =sum_of_multiples2(i,3) + sum_of_multiples2(i,5) - sum_of_multiples2(i,15)
    # print(a,b)
       