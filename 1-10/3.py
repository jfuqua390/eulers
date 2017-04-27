#####Largest prime factor#####
import math

# def allfactors(number):
#     i=2;
#     while i < number:
#         if(number % i == 0):
#             print(i)
#         i += 1
#
#
# print(lpf(13195))

def lpf(number):
    i = 2
    while i * i <= number:
        while number % i == 0 and number != i:
            number = number / i
        i = i + 1
    return number

print(lpf(36))
