import pandas as pd
import numpy as np


def sign_violation_magic_numbers(data_arr, sign_violation_theshold = 3):

    threshold = sign_violation_theshold

    data_arr_sorted = np.sort(data_arr)
    data_arr_unique = np.unique(data_arr)
    data_arr_unique_sorted = np.sort(data_arr_unique)

    pos_data_arr_unique_sorted = data_arr_unique_sorted[threshold:]
    neg_data_arr_unique_sorted = data_arr_unique_sorted[:-threshold]

    test_values = list(data_arr_unique_sorted[:threshold]) + list(data_arr_unique_sorted[-threshold:])

    sign_violating_magic_numbers = []
    if all(x > 0 for x in pos_data_arr_unique_sorted):
        sign_violating_magic_numbers.extend([val for val in test_values if val < 0])
    elif all(x < 0 for x in neg_data_arr_unique_sorted):
        sign_violating_magic_numbers.extend([val for val in test_values if val > 0])
    return sign_violating_magic_numbers

