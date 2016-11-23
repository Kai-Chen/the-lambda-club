def gcd(a, b):
    if a > b:
        return gcd(b, a)

    remainder = b % a
    if remainder == 0:
        return a
    return gcd(remainder, a)

