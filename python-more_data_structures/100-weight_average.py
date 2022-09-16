#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return 0
    sum_all_list = 0
    sum_div = 0
    for row in my_list:
        list_tuple = list(row)
        sum_tuple = 1
        for index in range(len(list_tuple)):
            if index == len(list_tuple) - 1 :
                sum_div += list_tuple[index]
            sum_tuple *= list_tuple[index]
        sum_all_list += sum_tuple
    return (sum_all_list / sum_div)
