import time

1DAY = 3600
1WEEk = 7*1DAY
1MONTH = 30*1DAY
3MONTH = 3*1MONTH

current_time = time()

FC_TSFRESH_TIME = {
    "approximate_entropy": [{'m': 2, 'r': 0.1},
                            {'m': 2, 'r': 0.3},
                            {'m': 2, 'r': 0.5},
                            {'m': 2, 'r': 0.7},
                            {'m': 2, 'r': 0.9}],
    "autocorrelation": [{'lag': 0},
                        {'lag': 1},
                        {'lag': 2},
                        {'lag': 3},
                        {'lag': 4}],
    "benford_correlation": None,
    "c3": [{'lag': 0},
            {'lag': 1},
            {'lag': 2},
            {'lag': 3},
            {'lag': 4}],
    "binned_entropy": [{'max_bins': 5}],
    "count_above_mean": None,
    "count_below_mean": None,
    "kurtosis": None,
    "mean": None,
    "mean_abs_change": None,
    "mean_change": None,
    "mean_second_derivative_central": None,
    "median": None,
    "quantile": [{'q': 99},
            {'q': 95},
            {'q': 90},
            {'q': 80},
            {'q': 20}],
    "ratio_beyond_r_sigma" : [{'r': 1},
            {'q': 2},
            {'q': 6}],
    "skewness": None,
    "standard_deviation": None,
    "variance": None,
    "variance_larger_than_standard_deviation": None,
    "variation_coefficient": None,
    "time_since_first": [{'current_time': current_time}],
    "time_since_last": [{'current_time': current_time}],
    "ratio_tx_time_since_time": 
        [{'current_time': current_time, "time": 1DAY},
        {'current_time': current_time, "time": 1WEEK}
        {'current_time': current_time, "time": 1MONTH}
        {'current_time': current_time, "time": 3MONTHS}],
    "ratio_tx_time_since_last_tx": 
        [{"time": 1DAY},
        {"time": 1WEEK}
        {"time": 1MONTH}
        {"time": 3MONTHS}],
    "ratio_above_mean": None
}

FC_TSFRESH_VALUE = {
    "abs_energy": None,
    "approximate_entropy": [{'m': 2, 'r': 0.1},
                            {'m': 2, 'r': 0.3},
                            {'m': 2, 'r': 0.5},
                            {'m': 2, 'r': 0.7},
                            {'m': 2, 'r': 0.9}],
    "autocorrelation": [{'lag': 0},
                        {'lag': 1},
                        {'lag': 2},
                        {'lag': 3},
                        {'lag': 4}],
    "benford_correlation": None,
    "binned_entropy": [{'max_bins': 5}],
    "count_above_mean": None,
    "count_below_mean": None,
    "has_duplicate": None,
    "maximum": None,
    "mean": None,
    "mean_abs_change": None,
    "mean_change": None,
    "mean_second_derivative_central": None,
    "median": None,
    "minimum": None,
    "skewness": None,
    "standard_deviation": None,
    "variance": None,
    "variance_larger_than_standard_deviation": None,
    "variation_coefficient": None,
}

FC_TSFRESH_GAS = {
    "abs_energy": None,
    "approximate_entropy": [{'m': 2, 'r': 0.1},
                            {'m': 2, 'r': 0.3},
                            {'m': 2, 'r': 0.5},
                            {'m': 2, 'r': 0.7},
                            {'m': 2, 'r': 0.9}],
    "autocorrelation": [{'lag': 0},
                        {'lag': 1},
                        {'lag': 2},
                        {'lag': 3},
                        {'lag': 4}],
    "benford_correlation": None,
    "binned_entropy": [{'max_bins': 5}],
    "count_above_mean": None,
    "count_below_mean": None,
    "has_duplicate": None,
    "maximum": None,
    "mean": None,
    "mean_abs_change": None,
    "mean_change": None,
    "mean_second_derivative_central": None,
    "median": None,
    "minimum": None,
    "skewness": None,
    "standard_deviation": None,
    "variance": None,
    "variance_larger_than_standard_deviation": None,
    "variation_coefficient": None,
}

FC_TSFRESH = {
    "timeStamp": FC_TSFRESH_TIME,
    "value": FC_TSFRESH_VALUE,
    "gas": FC_TSFRESH_GAS,
    "gasPrice": FC_TSFRESH_GAS
}


