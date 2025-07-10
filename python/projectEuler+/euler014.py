# time error
# count = 0
def collatz(n,count=0):
    if(n==1):
        return count
    count+=1
    if(n%2==0):
        return collatz(n/2,count)
    else:
        return collatz(3*n+1,count)
T = int(input())
for i in range(T):
    N = int(input())
    final_num = 1
    for j in range(1,N+1):
        if(collatz(j)>=collatz(final_num)):
            final_num = j
    
    print(final_num)
# print(collatz(18),collatz(19))