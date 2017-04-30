import numpy as np


def get_vector(data):
    data = np.reshape(data, len(data))  # Converts a two-dimensional array to a one-dimensional array
    sc_mean = np.mean(data)
    sc_median = np.median(data)
    sc_std = np.std(data)
    sc_min = np.min(data)
    sc_max = np.max(data)
    sc_range = sc_max-sc_min
    sc_min_ratio = sc_min/len(data)
    sc_max_ratio = sc_max/len(data)

    sc_diff_1th = np.diff(data)     # Calculate the 1-th discrete difference
    sc1diff_mean = np.mean(sc_diff_1th)
    sc1diff_median = np.median(sc_diff_1th)
    sc1diff_std = np.std(sc_diff_1th)
    sc1diff_min = np.min(sc_diff_1th)
    sc1diff_max = np.max(sc_diff_1th)
    sc1diff_range = sc1diff_max - sc1diff_min
    sc1diff_min_ratio = sc1diff_min / len(sc_diff_1th)
    sc1diff_max_ratio = sc1diff_max / len(sc_diff_1th)
    sc1adiff_mean = np.mean(np.fabs(sc_diff_1th))
    sc1gdiff_mean = sc1adiff_mean / sc_std

    sc_diff_2th = np.diff(data, 2)  # Calculate the 1-th discrete difference.
    sc2diff_mean = np.mean(sc_diff_2th)
    sc2diff_median = np.median(sc_diff_2th)
    sc2diff_std = np.std(sc_diff_2th)
    sc2diff_min = np.min(sc_diff_2th)
    sc2diff_max = np.max(sc_diff_2th)
    sc2diff_range = sc2diff_max - sc2diff_min
    sc2diff_min_ratio = sc2diff_min / len(sc_diff_2th)
    sc2diff_max_ratio = sc2diff_max / len(sc_diff_2th)
    sc2adiff_mean = np.mean(np.fabs(sc_diff_2th))
    sc2gdiff_mean = sc2adiff_mean / sc_std

    fft_data = np.fft.fft(data) # Calculate ftt data return complex array
    scfft_mean = np.mean(fft_data)
    scfft_median = np.median(fft_data)
    scfft_std = np.std(fft_data)
    scfft_min = np.min(fft_data)
    scfft_max = np.max(fft_data)
    scfft_range = scfft_max - scfft_min

    vector = [sc_mean, sc_median, sc_std, sc_min, sc_max, sc_range, sc_min_ratio, sc_max_ratio,
              sc1diff_mean, sc1diff_median, sc1diff_std, sc1diff_min, sc1diff_max,
              sc1diff_range, sc1diff_min_ratio, sc1diff_max_ratio, sc1adiff_mean, sc1gdiff_mean,
              sc2diff_mean, sc2diff_median, sc2diff_std, sc2diff_min, sc2diff_max,
              sc2diff_range, sc2diff_min_ratio, sc2diff_max_ratio, sc2adiff_mean, sc2gdiff_mean,
              scfft_mean, scfft_median, scfft_std, scfft_min, scfft_max, scfft_range
              ]
    return vector
