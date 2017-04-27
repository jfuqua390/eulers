def find_primes(n):
    primes = []
    for p in range(2,n+1):
        for i in range(2, p):
            if p % i == 0:
                break
        else:
            primes.append(p)

    return primes

print(find_primes(20))

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
