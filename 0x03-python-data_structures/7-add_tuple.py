#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result_list = [0, 0]

    for i in range(0, len(tuple_a)):
        if i == 2:
            break
        result_list[i] += tuple_a[i]

    for i in range(0, len(tuple_b)):
        if i == 2:
            break
        result_list[i] += tuple_b[i]
    return ((result_list[0], result_list[1]))
