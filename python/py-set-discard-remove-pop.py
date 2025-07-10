# failing testcases
N = int(input())
m_set = set(map(int,input().split(" ")))

N_op = int(input())
for i in range(N_op):
    user_inp = input().split(" ")
    match user_inp[0]:
        case "pop":
            m_set.pop()
        case "discard":
            m_set.discard(user_inp[1])
        case "remove":
            m_set.remove(user_inp[1])
print(len(m_set))