#!/usr/bin/python3
""" 6-peak Neque porro quisquam est qui dolorem ipsum quia dolor sit amet """


def find_peak(list_of_integers: list):
    """find_peak Neque porro quisquam est qui dolorem ipsum quia dolor sit amet"""
    if len(list_of_integers) is 0:
        return None

    if len(list_of_integers) is 1:
        return list_of_integers[0]

    max = list_of_integers[0]
    for n in list_of_integers:
        if n > max:
            max = n
    return max
