import math

def sieve_of_eratosthenes(limit = 125):
    sieve = [True] * limit
    sieve[0] = sieve[1] = False

    for (i, isprime) in enumerate(sieve):
        if (isprime):
            for n in range(i * i, limit, i):
                sieve[n] = False
    return sieve

print(sieve_of_eratosthenes(100))

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

print(find_prime(100))
