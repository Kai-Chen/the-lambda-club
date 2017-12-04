def max2(a,b):
    return a if a > b else b

def max3(a,b,c):
    return max2(max2(a,b),c)

def reverse(s):
    return s if len(s) <= 1 else reverse(s[1:]) + s[0]

def reverse2(s):
    return ''.join(reversed(s))
