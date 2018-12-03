#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: example_3_1.py
#    Created:       <2018/12/03 21:32:40>
#    Last Modified: <2018/12/03 21:45:36>

import tensorflow as tf

a = tf.constant(5)
b = tf.constant(2)
c = tf.multiply(a, b)
d = tf.add(a, b)
e = tf.subtract(c, d)
f = tf.add(c, d)
g = tf.divide(e, f)

with tf.Session() as sess:
    outs = sess.run(g)

print("outs = {}".format(outs))

a = tf.constant(5.0)
b = tf.constant(2.0)
c = tf.multiply(a, b)
d = tf.sin(c)
e = tf.divide(d, b)

with tf.Session() as sess:
    outs = sess.run(e)

print("outs = {}".format(outs))
