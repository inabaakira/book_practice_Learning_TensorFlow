#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: example_3_3.py
#    Created:       <2019/03/14 20:36:03>
#    Last Modified: <2019/03/14 20:41:49>

import tensorflow as tf
import numpy as np

c = tf.constant([[1, 2, 3],
                 [4, 5, 6]])
print("Python List input: {}".format(c.get_shape()))

c = tf.constant(np.array([
    [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 8, 7, 6]],

    [[1, 1, 1, 1],
     [2, 2, 2, 2],
     [3, 3, 3, 3]]
]))
print("3d NumPy array input: {}".format(c.get_shape()))
