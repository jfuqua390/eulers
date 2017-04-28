import math
import functools

def find_prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

print(find_prime_factors(8))

def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    print(a * b // gcd(a, b))
    return a * b // gcd(a, b)

def lcmm(*args):
    """Return lcm of args."""
    return functools.reduce(lcm, args)

def lcm_seq(seq):
    """Return lcm of sequence."""
    return functools.reduce(lcm, seq)

solution = lcm_seq(range(1,21))
print (lcmm(*range(1,20)))
