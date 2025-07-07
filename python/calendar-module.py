#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    format_string = "%a %d %b %Y %H:%M:%S %z"
    delta_time = abs(int(datetime.strptime(t2,format_string).timestamp()-datetime.strptime(t1,format_string).timestamp()))
    # delta_time = 0
    return delta_time

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)
        print(delta)
    #     fptr.write(delta + '\n')

    # fptr.close()
