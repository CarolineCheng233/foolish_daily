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


def random():
    # size: int or tuple
    # return random data in range [0.0, 1.0)
    array1 = np.random.random()
    array2 = np.random.random(size=1)
    array3 = np.random.random(size=(1, 2, 3))
    array4 = np.random.random_sample(size=(1, 2, 3))


def foo_numpy():
    choice()
    rand()
    random()


if __name__ == '__main__':
    foo_numpy()
