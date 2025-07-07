import operator
# incomplete
def person_lister(f):
    def inner(people):
       
        m_dict = {}
        age_list = []
        for i in people:
            age_list.append(i[2])
            m_dict[i[2]]=f(i)
        age_list.sort()
        name_list = [m_dict[i] for i in age_list ]
        return(name_list)
        
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')