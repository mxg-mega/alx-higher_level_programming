#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newList = []
    try:
        for i in range(list_length):
            div = 0
            try:
                div = my_list_1[i] / my_list_2[i]
            except ZeroDivisionError:
                print("division by 0")
                div = 0
            except TypeError:
                print("wrong type")
                div = 0
            except IndexError:
                print("out of range")
                div = 0
            newList.append(div)
    except ValueError:
        pass
    finally:
        return (newList)
