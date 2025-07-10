# Enter your code here. Read input from STDIN. Print output to STDOUT
from functools import lru_cache
import sys 
sys.setrecursionlimit(5000)
print(sys.getrecursionlimit())
@lru_cache(maxsize=999999)
def factorial(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*factorial(n-1)

T = int(input())
for i in range(T):
    array = list(map(int,input().split(" ")))
    print(int(factorial(array[0]+array[1])/(factorial(array[0])*factorial(array[1]))))