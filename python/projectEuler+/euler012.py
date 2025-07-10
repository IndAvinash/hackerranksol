# Not time efficient
from functools import lru_cache

@lru_cache(maxsize=8192)
def calculate_numdiv(num):
    numdiv = 1
    for i in range(2,int(num)+1):
        if num%i == 0:
            numdiv+=1
    return numdiv

T = int(input())

for i in range(T):
    N = int(input())
    numdiv = 1
    i = 1
    while numdiv<=N:
        triangle_num = i*(i+1)/2
        numdiv = calculate_numdiv(triangle_num)
        if(numdiv>N):
            print(int(triangle_num))
            break
        i+=1


# print(calculate_numdiv(2))/
        
        
    