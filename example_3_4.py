#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: example_3_4.py
#    Created:       <2019/03/14 21:05:25>
#    Last Modified: <2019/03/14 21:07:31>

import tensorflow as tf

sess = tf.InteractiveSession()
c = tf.linspace(0.0, 4.0, 5)
print("The content of 'c':\n{}\n".format(c.eval()))
sess.close()
