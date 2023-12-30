#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    best_key, best_value = None, float('-inf')

    for key, value in a_dictionary.items():
        if value > best_value:
            best_key, best_value = key, value

    return best_key
