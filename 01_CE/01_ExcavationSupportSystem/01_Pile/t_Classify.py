# -*- coding: utf-8 -*-
import numpy as np
def binary_search_np(A, B):
    # assume A and B are numpy arrays
    idx2 = np.minimum(len(A) - 1, np.searchsorted(A, B)) 
    idx1 = np.maximum(0, idx2 - 1)
    idx2_is_better = np.abs(A[idx1] - B) > np.abs(A[idx2] - B)
    np.putmask(idx1, idx2_is_better, idx2)
    return A[idx1]

a = []
np_CIP = np.array(t_CIP)
np_H = np.array(t_H)

np_set = binary_search_np(np_CIP, np_H)
converted_set = sorted(set(np_set))

for item in converted_set:
    idx = t_CIP.index(item)
    a.append(idx)

print(a)