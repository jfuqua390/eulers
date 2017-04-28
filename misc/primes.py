def find_primes(n):
    primes = []
    for p in range(2,n+1):
        for i in range(2, p):
            if p % i == 0:
                break
        else:
            primes.append(p)

    return primes

print(find_primes(5000))

def rwh_primes2(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    correction = (n%6>1)
    n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
    sieve = [True] * (n/3)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      ((k*k)/3)      ::2*k]=[False]*((n/6-(k*k)/6-1)/k+1)
        sieve[(k*k+4*k-2*k*(i&1))/3::2*k]=[False]*((n/6-(k*k+4*k-2*k*(i&1))/6-1)/k+1)
    return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]

def sieve2(n):
    loops = 0
    numbers = range(0, n)
    for prime in numbers:
        if prime < 2:
            continue
        elif prime > n ** 0.5:
            break
        for i in range(prime ** 2, n, prime):
            numbers[i] = 0
            loops += 1
    return [x for x in numbers if x > 1], loops

def sieve_of_eratosthenes(limit = 125):
    sieve = [True] * limit
    sieve[0] = sieve[1] = False

    for (i, isprime) in enumerate(sieve):
        if (isprime):
            for n in range(i * i, limit, i):
                sieve[n] = False
    return sieve
    
