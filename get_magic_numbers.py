import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import gaussian_kde
from pprint import pprint
from scipy.integrate import simpson
from collections import Counter
import logging
logging.basicConfig(level=logging.DEBUG)

from string_magic_numbers import magic_strings_detection as string_values_process
from sign_violation_magic_numbers import sign_violation_magic_numbers as opposite_sign_process
from distance_based_magic_numbers import delta_distributed_magic_numbers 
from identical_magic_numbers import identical_column_magic_numbers as all_values_are_same
from magic_dictionaries import magic_dictionary, add_to_master_dict, safe_concatenate, clean_magic_results  
from density_plot import plot_data_density


def get_magic_numbers_main(df, extended_col_info, sign_violation_theshold = 3,gauss_threshold = 0.01,  overlap_threshold=5.0, plot_graphs = True):

    rows, columns = df.shape
    master_dict = {}

    for col in range(columns):

        results_dict = {}

        magic_strings = [] # Process 1
        magic_sign_violation = [] # Process 2
        magic_distanced_numbers = [] # Process 3
        all_magic_numbers = None # Process 4

        data_array = np.array(df.iloc[:, col]) # extract from the df the array
        # Determine what type of values are in the array
        value_type = str(extended_col_info[col][1])
        col_name = extended_col_info[col][0]

        # This process may be inaccurate on small datasets. For optimal statistical reliability, adjust the array_length parameter
        array_length = len(data_array)
        if (value_type == "N") and (array_length > 0): 

            data_arr, magic_strings = string_values_process(data_array) # Process 1 

            data_arr = data_arr[~np.isnan(data_arr) & (data_arr != '') & (data_arr != ' ')] # Clean the data array further

            all_magic_numbers = all_values_are_same(data_arr) # Process 4

            if (all_magic_numbers == False) and (len(data_arr) > 0):

                magic_sign_violation = opposite_sign_process(data_arr, sign_violation_theshold) # Process 2

                magic_distanced_numbers_arrays = delta_distributed_magic_numbers(data_arr, col_name, gauss_threshold,  overlap_threshold, plot_graphs) # Process 3
                magic_distanced_numbers = safe_concatenate(magic_distanced_numbers_arrays)

                plot_data_density(data_arr, col_name, plot_graphs)

            #print_magic_results(magic_strings, magic_sign_violation, magic_distanced_numbers, all_magic_numbers, col_name)

            
        results_dict = magic_dictionary(magic_strings, magic_sign_violation, magic_distanced_numbers, all_magic_numbers, col_name)

        master_dict = add_to_master_dict(master_dict, results_dict)

        cleaned_dict = clean_magic_results(master_dict)

    return master_dict, cleaned_dict