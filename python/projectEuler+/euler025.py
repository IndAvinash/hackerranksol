# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from functools import lru_cache
sys.set_int_max_str_digits(5001)
@lru_cache(maxsize=4096)
def fib(length):
    a = 0
    b = 1
    i = 0
    while len(str(a))<length:
        a,b = b,a+b
        i+=1
    return i
        
        
        
        
T = int(input())
for i in range(T):
    N = int(input())
    print(fib(N))
