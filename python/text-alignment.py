# printing HackerRank logo
# https://www.hackerrank.com/challenges/text-alignment/problem


a = f'''    H    
   HHH   
  HHHHH  
 HHHHHHH 
HHHHHHHHH
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
                    HHHHHHHHH 
                     HHHHHHH  
                      HHHHH   
                       HHH    
                        H '''

def part1(n):
    for i in range(1, 2*n,2):
        print(('H'*i).center(2*n-1, " "))


def part2(n):
    for i in range(1, n+1):
        a = (" "*((n-1)//2)+'H'*n+" "*((n-1)//2))
        print(a+" "*(2*n+1)+a)
def part3(n):
    for i in range((n+1)//2):
        print((" "*((n-1)//2)+('H'*n*5)))
def part4(n):
    for i in range(1, 2*n,2):
        print(" "*(4*n-1),('H'*(2*n-i)).center(2*n-1, " "))
        # print(('H'*(2*n-i)).center(2*n-1, " "))
part1(5)
part2(5)
part3(5)
part2(5)
part4(5)
# print(a)