import math

def pal(n):
    if len(str(n)) == 4:
        if int(str(n)[0]) - int(str(n)[3]) + int(str(n)[1]) - int(str(n)[2]) == 0:
            return True
        else:
            return False
    return False;

print(pal(91*99))

def findLargestPal():
    a = 10
    b = 99
    result=0
    for a in range(10, 99):
        for b in range(10, 99):
            if pal(a*b) and result < a*b:
                result = a*b
    return result

print(findLargestPal())

def num_digits(num):
    ori = num
    digs = 0
    while ori > 0:
        ori = ori // 10
        digs += 1

    return digs
