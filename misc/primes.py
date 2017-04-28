def find_primes(n):
    primes = []
    for p in range(2,n+1):
        for i in range(2, p):
            if p % i == 0:
                break
        else:
            primes.append(p)

    return primes

print(find_primes(17))
