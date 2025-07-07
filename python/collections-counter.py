# from collections import Counter

# no. of shoes
num_shoes = int(input())
# list of sizes
size_list = list(map(int,input().split(" ")))
# num of customers
m = []
earning = 0
for i in range(int(input())):
    size_amt = list(map(int,input().split(" ")))
    if(size_amt[0] in size_list):
        size_list.remove(size_amt[0])
        earning+=size_amt[1]
    
print(earning)
    

