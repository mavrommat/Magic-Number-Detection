
import pandas as pd
import numpy as np

def magic_dictionary(magic_strings, magic_opp_sign_numbers, magic_distanced_numbers, all_magic_numbers, col_name):
    
    return {
        'column_name': col_name,
        'magic_strings': magic_strings,
        'magic_opp_sign_numbers': magic_opp_sign_numbers,
        'magic_distanced_numbers': magic_distanced_numbers,
        'all_magic_numbers': all_magic_numbers
    }

def add_to_master_dict(master_dict, results_dict):
    col_name = results_dict['column_name']
    master_dict[col_name] = {
        'magic_strings': results_dict['magic_strings'],
        'magic_opp_sign_numbers': results_dict['magic_opp_sign_numbers'],
        'magic_distanced_numbers': results_dict['magic_distanced_numbers'],
        'all_magic_numbers': results_dict['all_magic_numbers']
    }
    return master_dict

def safe_concatenate(nested_arrays):
    valid_arrays = []
    
    for arr in nested_arrays:
        if arr is None:
            continue
            
        if isinstance(arr, (np.number, int, float, np.float64, np.int64)):
            valid_arrays.append(np.array([arr]))
            
        elif hasattr(arr, '__len__') and len(arr) > 0:
            arr_np = np.array(arr)
            valid_arrays.append(arr_np.ravel())
            
        elif hasattr(arr, '__len__') and len(arr) == 0:
            continue
    
    if len(valid_arrays) == 0:
        return np.array([])
    
    return np.concatenate(valid_arrays)