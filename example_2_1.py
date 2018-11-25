#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: example_2_1.py
#    Created:       <2018/11/26 01:28:06>
#    Last Modified: <2018/11/26 01:38:53>

import tensorflow as tf

h = tf.constant("Hello")
w = tf.constant(" World!")
hw = h + w

with tf.Session() as sess:
    ans = sess.run(hw)

print(ans)
