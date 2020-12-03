# -*- coding:utf-8 -*-


import numpy as np


def choice():
    array = np.array(['1', '2', '3', '4', '5'])
    # choose items directly from array without duplicated items(replace=False)
    items = np.random.choice(a=array, size=3, replace=False)

    # choose idxes from arange[0, 10) with possible duplicated idx(replace=True)
    idxes = np.random.choice(a=10, size=5)


def rand():
    # give any shape to generate [0, 1) uniform distributed data
    array = np.random.rand(4, 3, 2)  # shape:(4, 3, 2)
    array2 = np.random.rand(1, 2, 3, 4, 5)  # shape:(1, 2, 3, 4, 5)


def foo_numpy():
    choice()
    rand()


if __name__ == '__main__':
    foo_numpy()
