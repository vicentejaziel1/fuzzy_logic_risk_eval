import numpy as np
import generic_functions as gp


def syntetics(matrix):
    row_sum = np.sum(matrix, axis=1)
    sum = np.sum(row_sum, axis=0)
    inv_sum = gp.inverse(sum)
    not_rounded = np.multiply(row_sum, inv_sum)

    return np.around(not_rounded, decimals=3)


def weights(matrix):
    sn = syntetics(matrix)

    d = []
    w = []
    for i, ki in enumerate(sn):
        for j, kj in enumerate(sn):
            if (i != j):
                if (ki[1] >= kj[1]):
                    d.append(1)
                elif (kj[0] >= ki[2]):
                    d.append(0)
                else:
                    v = (kj[0] - ki[2]) / ((ki[1] - ki[2]) - (kj[1] - kj[0]))
                    d.append(v)
        w.append(min(d))
        d = []

    return w