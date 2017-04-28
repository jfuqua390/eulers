def remove_dupe (list):
    s = []
    for i in list:
        if i not in s:
            s.extend(i)
    return s
