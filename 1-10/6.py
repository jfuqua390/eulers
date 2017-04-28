import math

def sum_squares(range):
    i = 0
    result = 0
    while i < range + 1:
        result += i * i
        i+=1
    return result

def square_sum(range):
    i = 0
    result = 0
    while i < range+1:
        result += i
        i+=1
    return result * result

def find_dif(range):
    return square_sum(range) - sum_squares(range)

print(find_dif(100))
