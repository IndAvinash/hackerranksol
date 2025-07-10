px = list(map(int,input().split(" "))) #[x,k]-> p(x)= k
polynomial  = input()
print(eval(polynomial.replace("x",str(px[0])))==px[1])
