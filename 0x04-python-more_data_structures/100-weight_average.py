
#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    num = 0
    den = 0

    for wup in my_list:
        num += wup[0] * wup[1]
        den += wup[1]

    return (num / den)
