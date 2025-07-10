#!/bin/python3

import sys
from functools import reduce


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    prod = 0
    for i in range(len(num)-k+1):
        nums = list(map(num[i:i+k].split("")))
        temp_prod = reduce(lambda x, y: x * y,nums)
        if(prod<temp_prod):
            prod=temp_prod

    print(prod)