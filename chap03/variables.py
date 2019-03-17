#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: variables.py
#    Created:       <2019/03/17 12:42:01>
#    Last Modified: <2019/03/17 13:53:34>

import tensorflow as tf

init_val = tf.random_normal((1, 5), 0, 1)
var = tf.Variable(init_val, name='var')
print("pre run:\n{}".format(var))

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    post_var = sess.run(var)

print("\npost run:\n{}".format(post_var))

var = tf.Variable(init_val, name='var')
print("pre run:\n{}".format(var))
