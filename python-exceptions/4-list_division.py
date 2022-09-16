#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for idx in range(list_length):
        try:
            new_item = my_list_1[idx] / my_list_2[idx]
        except ZeroDivisionError:
            print("division by 0")
            new_item = 0
        except TypeError:
            print("wrong type")
            new_item = 0
        except IndexError:
            print("out of range")
            new_item = 0
        finally:
            new_list.append(new_item)
    return new_list
