def num_digits(num):
    ori = num
    digs = 0
    while ori > 0:
        ori = ori // 10
        digs += 1

    return digs

print(num_digits(4004929))
