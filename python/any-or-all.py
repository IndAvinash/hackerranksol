N = input()
m_list = list(map(int,input().strip().split(' ')))
print(all(a>0 for a in m_list)>0 and any(str(i)==str(i)[::-1] for i in m_list))
# 3 Lines code challenge completed