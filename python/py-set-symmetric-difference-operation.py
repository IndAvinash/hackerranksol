m_list = []
for i in range(2):
    N = input()
    elem = set(map(int,input().split(" ")))
    m_list.append(elem)


def symmetric_def(a,b):
    return (a.union(b)).difference(a.intersection(b))
print(len(symmetric_def(m_list[0],m_list[1])))
