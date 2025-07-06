def print_formatted(number):
    num = len(bin(number).replace("0b",""))
    for i in range(1,number+1):
        
        print(str(i).rjust(num),
              oct(i).replace("0o","").rjust(num),
              hex(i).replace("0x","").upper().rjust(num),
              bin(i).replace("0b","").rjust(num))

        
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)