def gcd(a, b):
    """Return the Greatest Common Divisor of two numbers.

    Implements the Euclidean algorithm.
    """
    if a > b:
        return gcd(b, a)
    return b if a == 0 else gcd(b % a, a)

import math
def newton_sqrt(x):
    def next_guess(y): return (y + (x/y)) / 2
    def approx(y):
        return y if math.isclose(x, y*y) else approx(next_guess(y))
    return approx(1)
