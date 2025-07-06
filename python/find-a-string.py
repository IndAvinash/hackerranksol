# 06/07/2025
def count_substring(string, sub_string):
    i=0
    for s in range(len(string)):
        if(string[s]==sub_string[0] and (string[s:s+len(sub_string)]==sub_string)):
            i+=1
    return i

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)