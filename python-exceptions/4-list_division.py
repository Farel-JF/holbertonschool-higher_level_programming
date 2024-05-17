#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    New_list = []
    for i in range(list_length):
        try:
            if i < len(my_list_1) and i < len(my_list_2):
                result = my_list_1[i] / my_list_2[i]
            else:
                result = 0
                print("out of range")
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except (TypeError, ValueError):
            result = 0
            print("wrong type")
        finally:
            New_list.append(result)
    return New_list
