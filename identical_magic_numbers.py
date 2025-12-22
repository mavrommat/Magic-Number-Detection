import numpy as np


def identical_column_magic_numbers(data_arr):

    if isinstance(data_arr, np.ndarray):
        if data_arr.size == 0:  # Handle empty NumPy array
            return False
        return data_arr[0] if np.all(data_arr == data_arr[0]) else False
    else:  # Handle regular Python list
        if not data_arr:  # Handle empty list
            return False
        return data_arr[0] if all(x == data_arr[0] for x in data_arr) else False