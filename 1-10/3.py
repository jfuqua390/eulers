#####Largest prime factor#####
import math

def lpf(number):
    i = 2
    while i * i <= number:
        while number % i == 0 and number != i:
            number = number / i
        i = i + 1
    return number

print(lpf(600851475143))
