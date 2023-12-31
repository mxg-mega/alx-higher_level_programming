#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    units_dict = {"I":1, "II":2, "III":3, "IV":4, "V":5, "VI":6, "VII":7, "VIII":8, "IX":9}
    tens_dict = {"X":10, "XX":20, "XXX":30, "XL":40, "L":50, "LX":60, "LXX":70, "LXXX":80, "XC":90}
    hundreds_dict = {"C":100, "CC":200, "CCC":300, "CD":400, "D":500,
                    "DC":600, "DCC":700, "DCCC":800, "CM":900}
    thousands_dict = {"M":1000, "MM":2000, "MMM":3000}
    holder = ''
    num, th, h, t, u = 0, 0, 0, 0, 0
    for i in roman_string.upper():
        if i in thousands_dict.keys():
            if holder != '':
                holder += i
                if holder in hundreds_dict.keys():
                    h = hundreds_dict[holder]
                    continue
            else: 
                holder = holder + i
                th = thousands_dict[holder]
        elif i in hundreds_dict.keys():
            if holder != '':
                if holder in hundreds_dict.keys():
                    holder += i
                else:
                    holder += i
                    if holder in tens_dict.keys():
                        t = tens_dict[holder]
                        continue
                    else:
                        holder = ''
                        holder += i
                h = hundreds_dict[holder]
            else:
                holder += i
                h = hundreds_dict[holder]
        elif i in tens_dict.keys():
            if holder != '':
                if holder in tens_dict.keys():
                    holder += i
                else:
                    holder += i
                    if holder in units_dict.keys():
                        u = units_dict[holder]
                        continue
                    else:
                        holder = ''
                        holder += i
                t = tens_dict[holder]
            else:
                holder += i
                t = tens_dict[holder]
        elif i in units_dict.keys():
            if holder != '':
                if holder in units_dict.keys():
                    holder += i
                else:
                    holder = ''
                    holder += i
                u = units_dict[holder]
            else:
                holder += i
                u = units_dict[holder]
    num = th + h + t + u
    return num
