#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: example_3_2.py
#    Created:       <2019/03/13 13:30:56>
#    Last Modified: <2019/03/13 13:43:34>

import tensorflow as tf

a = tf.constant(5)
b = tf.constant(2)
c = tf.constant(3)

d = tf.multiply(a, b)
e = tf.add(c, b)
f = tf.subtract(d, e)

with tf.Session() as sess:
    fetches = [a, b, c, d, e, f]
    outs = sess.run(fetches)

print("outs = {}".format(outs))
print(type(outs[0]))
