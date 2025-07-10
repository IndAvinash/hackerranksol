cube = lambda x: x**3 

def fibonacci(n):
    i = 0
    a = 0
    b=1
    m_list = list()
    while i < n:
        m_list.append(a)
        a,b = b,a+b
        i+=1
    return m_list
    

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))