def gcd(a, b):
    if a > b:
        return gcd(b, a)

    remainder = b % a
    if remainder == 0:
        return a
    return gcd(remainder, a)

import math
def newton_sqrt(x):
    def next_guess(y): return (y + (x/y)) / 2
    def approx(y):
        return y if math.isclose(x, y*y) else approx(next_guess(y))
    return approx(1)
