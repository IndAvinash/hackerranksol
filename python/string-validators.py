# 06/07/2025
if __name__ == '__main__':
    s = input()
    isalnum = False
    isalpha = False
    isdigit= False
    isLower = False
    isUpper = False
    for i in s:
        if(i.isalnum()):
            isalnum = True
            break
    for i in s:
        if(i.isalpha()):
            isalpha = True
            break
    for i in s:
        if(i.isdigit()):
            isdigit = True
            break
    for i in s:
        if(i.islower()):
            isLower = True
            break
    for i in s:
        if(i.isupper()):
            isUpper = True
            break
    print(isalnum)
    print(isalpha)
    print(isdigit)
    print(isLower)
    print(isUpper)
# 06/07/2025
def method2():
    s = input().strip()
    isalnum = any(c.isalnum() for c in s)
    isalpha = any(c.isalpha() for c in s)
    isdigit = any(c.isdigit() for c in s)
    isLower = any(c.islower() for c in s)
    isUpper = any(c.isupper() for c in s)

    print(isalnum)
    print(isalpha)
    print(isdigit)
    print(isLower)
    print(isUpper)