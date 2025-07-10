#!/bin/python3
# optimize it for less time
import sys
from math import ceil
from functools import lru_cache
@lru_cache
def isPrime(num):
    sqrt = ceil(num**0.5)
    if(num<=2):
        return False if num!=2 else True
    if(num>2):
        i=2
        while i<=sqrt:
            if(num%i == 0):
                return False
            i+=1
        return True
    
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sums = 0
    for i in range(2,n+1):
        if isPrime(i):
            sums+=i
            
    print(sums)
# print(isPrime(5))