# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

# m_

def print_rangoli(size):
    string = "abcdefghijklmnopqrstuvwxyz"
    # sub_str = string[0:size]
    m_list = [a for a in string[0:size]]
    for i in range(len(m_list)*2-1):
        index = abs((len(m_list)-1-i))%len(m_list)
        fin_list = m_list[len(m_list):index:-1] + m_list[index:len(m_list)]
        print("-".join(fin_list).center(4*size-3,"-"))




if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)