#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: placeholders.py
#    Created:       <2019/03/19 13:28:13>
#    Last Modified: <2019/03/19 14:04:09>

import tensorflow as tf
import numpy as np

x_data = np.random.randn(5, 10)
w_data = np.random.randn(10, 1)

with tf.Graph().as_default():
    x = tf.placeholder(tf.float32, shape=(5, 10))
    w = tf.placeholder(tf.float32, shape=(10, 1))
    b = tf.fill((5, 1), -1.)
    xw = tf.matmul(x, w)

    xwb = xw + b
    s = tf.reduce_max(xwb)
    with tf.Session() as sess:
        # outs = sess.run(x, feed_dict={x: x_data})
        # outs = sess.run(w, feed_dict={w: w_data})
        # outs = sess.run(b)
        # outs = sess.run(xw, feed_dict={x: x_data, w: w_data})
        # outs = sess.run(xwb, feed_dict={x: x_data, w: w_data})
        outs = sess.run(s, feed_dict={x: x_data, w: w_data})

print("outs = {}".format(outs))

