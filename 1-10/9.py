def is_trip(a, b, c):
    if(a < b and b < c):
        if(a*a + b*b == c*c):
            return True
    return False

def find_trip_for_range (n):
    a = 3
    for i in range(a, 100):
        if(i % 2 == 0):
            a = i
            b = (a / 2) * (a / 2) - 1
            c = b + 2
            print('TestingEvens:', a, b, c, a+b+c)
            if(is_trip(a, b, c) and a + b + c == n):
                return('This is yo numbah:', a, b, c, '=', a*b*c)
        else:
            a = i
            b = (a*a - 1) / 2
            c = b + 1
            print('TestingOdds:', a, b, c, a+b+c)
            if(is_trip(a, b, c) and a + b + c == n):
                return('This could be yo numbah:', a, b, c,'=', a*b*c)


def find_trip_for_range2(n):
    for a in range(1, n):
        for b in range(a, n - a):
            c = n - a - b
            if(c < b):
                break
            if is_trip(a, b, c):
                print(a, b, c)
                print("Product:", a*b*c)

print(find_trip_for_range2(1000))
