#!/usr/bin/python3
def multiple_returns(sentence):
    my_list = []
    if len(sentence) < 1:
        my_list.append(None)
        my_list.append('')
    else:
        my_list.append(len(sentence))
        my_list.append(sentence[0])
    my_tuple = my_list[:]
    return (my_tuple)
