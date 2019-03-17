#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: names.py
#    Created:       <2019/03/17 04:38:04>
#    Last Modified: <2019/03/17 04:40:09>

import tensorflow as tf

with tf.Graph().as_default():
    c1 = tf.constant(4, dtype=tf.float64, name='c')
    c2 = tf.constant(4, dtype=tf.int32, name='c')
print(c1.name)
print(c2.name)
