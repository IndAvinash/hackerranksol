from functools import reduce
def average(array):
    m_set = set(array)
    m_set = list(m_set)
    n = len(m_set)
    sum = reduce(lambda x,y : x+y,m_set)
    return sum/n


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)