import numpy as np

def inverse(fn):
    inv = [1 / fn[2], 1 / fn[1], 1 / fn[0]]
    return inv


def normalize(array):
    s = sum(array)
    norm = np.divide(array, s)

    return norm