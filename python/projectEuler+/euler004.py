#!/bin/python3
def is_palindrome(n):
    return str(n) == str(n)[::-1]

palindromes = []
for i in range(100, 1000):
    for j in range(i, 1000): 
        prod = i * j
        if is_palindrome(prod):
            palindromes.append(prod)
palindromes = sorted(set(palindromes))
t = int(input())
for _ in range(t):
    n = int(input())
    ans = 0
    for p in palindromes:
        if p < n:
            ans = p
        else:
            break
    print(ans)
