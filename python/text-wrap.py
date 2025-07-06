import textwrap
# 06/07/2025 without textwrap
def wrap(string, max_width):
    m_list = []
    for i in range(0,len(string),max_width):
        m_list.append(string[i:i+max_width])
    return "\n".join(m_list)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


