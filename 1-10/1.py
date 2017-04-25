import math

def multiples(index, maxi):
    mylist = []
    count = maxi // index
    if(maxi % index == 0):
        for x in range(0, count):
            a = x * index
            mylist.append(a)
    else:
        for x in range(0, count+1):
            a = x * index
            mylist.append(a)
    
    return mylist

print(sum(multiples(5, 1000)) + sum(multiples(3,1000)))

print(multiples(4,20))
