def gcd(a, b):
    if a == b == 0:
        print('a и b должны быть не равны нулю.')
        return
    if b == 0:
        return abs(a)
    r = a % b
    return gcd(b, r)

print(gcd(7, 49))