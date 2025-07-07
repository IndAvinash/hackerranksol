from itertools import product


A = list(map(int,input().split(" ")))
B = list(map(int,input().split(" ")))
print(A)
m_list = list(product(A,B))
print(*m_list,sep=" ")
