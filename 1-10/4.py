import math

def is_palindrome(number):
    rev = 0
    ori = number
    while ori > 0:
        rev = rev * 10 + (ori % 10)
        ori = ori // 10

    return rev == number

print(is_palindrome(8008))

def find_palindrome_max_multiples(minimum, maximum):
    largest_palindrome = 0
    for i in range(minimum, maximum):
        for j in range(minimum, maximum):
            if is_palindrome(i * j) and (i * j > largest_palindrome):
                largest_palindrome = i * j

    return largest_palindrome

print(find_palindrome_max_multiples(100, 1000))
