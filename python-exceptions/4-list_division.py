#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            if i < len(my_list_1) and i < len(my_list_2):
                result.append(my_list_1[i] / my_list_2[i])
            else:
                result.append(0)
                print("out of range")
        except ZeroDivisionError:
            result.append(0)
            print("division by 0")
        except (TypeError, ValueError):
            result.append(0)
            print("wrong type")
    return result
