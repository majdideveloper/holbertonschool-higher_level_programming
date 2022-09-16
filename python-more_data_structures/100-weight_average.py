#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return 0
    sum_all_list = 0
    sum_div = 0
    i = 1
    for row in my_list:
        list_tuple = list(row)
        sum_tuple = 1
        for item in list_tuple:
            if item == list_tuple[-1] and i != len(my_list):
                sum_div += item
            sum_tuple *= item
        sum_all_list += sum_tuple
        i += 1
    return (sum_all_list / sum_div)
