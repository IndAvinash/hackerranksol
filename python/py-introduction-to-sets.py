from functools import reduce
def average(array):
    m_set = set(array)
    reduce(lambda x,y : x+y,m_set)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)