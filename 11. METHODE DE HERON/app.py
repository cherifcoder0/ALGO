from math import sqrt

def heron(n, p):
    if n < 0:
        raise ValueError("n doit être un entier naturel (>= 0)")
    if n == 0:
        return 0
    
    u = n
    while abs(u - sqrt(n)) > p:
        u = 0.5 * (u + n/u)
    return u

