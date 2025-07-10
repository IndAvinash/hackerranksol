m_list = []
for i in range(2):
    N = input()
    elem = set(map(int,input().split(" ")))
    m_list.append(elem)
print(len(m_list[0].intersection(m_list[1])))
