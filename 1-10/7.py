import math

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True

def find_prime(pos):
    primes = []
    i = 2
    result = 0
    while len(primes) < pos:
        if is_prime(i) and i > result:
            result = i
            primes.append(i)
        i+=1
    return result

print(find_prime(10001))
