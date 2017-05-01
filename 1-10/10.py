#Summation of Primes

#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.

from eulers.misc import primes

def sum_primes(range):
    primes = sieve_of_eratosthenes(range)
    return(primes)

print(sum_primes(10))
