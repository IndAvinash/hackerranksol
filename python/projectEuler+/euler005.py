#!/bin/python3

import sys

def lcm(a,b):
    if(b>a):
        a,b = b,a
    if(a==b):
        return a
    if(a>b):
        temp_b = b
        temp_a = a
        while not temp_a%temp_b==0:

            temp_a,temp_b= temp_b,temp_a%temp_b
        return (a*b)/temp_b
        
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    final_lcm = 1
    for i in range(1,n+1):
        final_lcm = lcm(final_lcm,i)
    print(int(final_lcm))
         