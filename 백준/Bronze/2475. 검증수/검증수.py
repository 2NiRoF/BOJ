def verify_num(a, b, c, d, e):
    n=0
    n += a**2
    n += b**2
    n += c**2
    n += d**2
    n += e**2
    return n%10

a, b, c, d, e = [int(i) for i in input().split()]
print(verify_num(a,b,c,d,e))