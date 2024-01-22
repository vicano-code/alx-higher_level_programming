#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    newlist = []
    for i in range(list_length):
        try:
            val = 0
            val = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            newlist.append(val)
    return newlist
